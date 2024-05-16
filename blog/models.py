from django.db import models

NULLABLE = {'null': True, 'blank': True}


class BlogRecord(models.Model):
    title = models.CharField(max_length=150, verbose_name='название', )
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    body = models.TextField(verbose_name='содержимое', **NULLABLE)
    picture = models.ImageField(upload_to='bloglpictures', verbose_name='фото', **NULLABLE)
    published_at = models.DateField(verbose_name='дата публикации', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')
    view_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
        ordering = ["published_at"]
