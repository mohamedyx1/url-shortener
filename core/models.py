from django.db import models
from django.urls import reverse


class Entry(models.Model):
    url = models.URLField()
    code = models.CharField(max_length=8, unique=True)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"code": self.code})


class Visit(models.Model):
    ip = models.GenericIPAddressField()
    country = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name="visits")
