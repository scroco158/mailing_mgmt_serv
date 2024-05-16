from django.urls import path
from .apps import BlogConfig
from .views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, status_change

app_name = BlogConfig.name

urlpatterns = [

    path('create/', BlogCreateView.as_view(), name='create_record'),
    path('', BlogListView.as_view(), name='list'),
    path('one_record/<int:pk>', BlogDetailView.as_view(), name='one_record'),
    path('edit/<int:pk>', BlogUpdateView.as_view(), name='update_record'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete_record'),
    path('status_change/<int:pk>', status_change, name='status_change'),

]
