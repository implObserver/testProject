from django.contrib.auth.models import Group
from django.db import models
from django.urls import reverse


class Url(models.Model):
    title = models.URLField()

    def get_absolute_url(self):
        return reverse('url', kwargs={"url_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URL'
        ordering = ['title']


class PermGroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.PROTECT, verbose_name='Группа')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    urls = models.ManyToManyField(Url, related_name="members", blank=True)

    def get_absolute_url(self):
        return reverse('main', kwargs={"pk": self.pk})

    def __str__(self):
        return self.group.name

    class Meta:
        verbose_name = 'Доступные ссылки'
        verbose_name_plural = 'Доступные ссылки'
        ordering = ['-created_at']
