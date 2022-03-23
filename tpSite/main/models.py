from django.db import models
from django.urls import reverse

from users.models import CustomUser


class Url(models.Model):
    url = models.URLField()
    members = models.ManyToManyField(CustomUser, related_name="members", blank=True)

    def get_absolute_url(self):
        return reverse('main', kwargs={"pk": self.pk})

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'Разграничение доступа к URL'
