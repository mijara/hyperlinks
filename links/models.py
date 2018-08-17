from django.db import models
from django.urls import reverse_lazy


class Link(models.Model):
    title = models.CharField(max_length=256)

    url = models.URLField(unique=True)

    keywords = models.CharField(max_length=2048, null=True, blank=True)

    description = models.CharField(max_length=2048, null=True, blank=True)

    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-create_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('links:link_detail', args=[self.pk])
