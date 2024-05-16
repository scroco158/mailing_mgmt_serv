from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify
from blog.models import BlogRecord
from blog.services import send_information_mail


class BlogCreateView(CreateView):
    model = BlogRecord
    fields = ('title', 'body', 'picture', 'published_at', 'is_published')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_rec = form.save()
            new_rec.slug = slugify(new_rec.title)
            new_rec.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = BlogRecord

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = BlogRecord

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        if self.object.view_count == 30:              # отправка письма по достижению
            send_information_mail(self.object.title)  # определенного кол-ва просмотров
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = BlogRecord
    fields = ('title', 'body', 'picture', 'published_at', 'is_published')
    success_url = reverse_lazy('blog:list')

    def get_success_url(self):
        return reverse('blog:one_record', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = BlogRecord
    success_url = reverse_lazy('blog:list')


def status_change(request, pk):
    one_rec = get_object_or_404(BlogRecord, pk=pk)
    if one_rec.is_published:
        one_rec.is_published = False
    else:
        one_rec.is_published = True
    one_rec.save()
    return redirect(reverse('blog:list'))
