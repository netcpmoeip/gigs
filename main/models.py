from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


class Page(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255)
    photo = models.ImageField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Страницы'
        verbose_name = 'Страница'

class Leg(models.Model):
    title = models.CharField(max_length=255)
    departure = models.DateTimeField('Departure', default=datetime.now())
    price = models.PositiveIntegerField('Price, Rub', default=0, null=True, blank=True)
    description = RichTextField()
    photo = models.ImageField(upload_to='uploads/', null=True, blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Походы'
        verbose_name = 'Поход'

    
class News(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    slug = models.SlugField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'
