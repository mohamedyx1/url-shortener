from django.db import models
from django.urls import reverse


class Entry(models.Model):
    url = models.URLField()
    code = models.CharField(max_length=8, unique=True)
    hits = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"code": self.code})
