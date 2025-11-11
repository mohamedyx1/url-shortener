import random
import string

from django.db import models
from django.urls import reverse


class Entry(models.Model):
    url = models.URLField()
    code = models.CharField(max_length=8)
    hits = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = "".join(
                random.choices(string.ascii_letters + string.digits, k=8)
            )
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"code": self.code})
