import random
import string

from django.db import models


class Entry(models.Model):
    url = models.URLField()
    code = models.CharField(max_length=8)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        return super().save(*args, **kwargs)
