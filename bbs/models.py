from django.db import models
from django.utils import timezone

class Topic(models.Model):

    dt      = models.DateTimeField(verbose_name="投稿日",default=timezone.now)
    comment = models.CharField(verbose_name="コメント",max_length=2000)

    def __str__(self):
        return self.comment
