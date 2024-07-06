from django.db import models


# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.CharField(max_length=60)
    created_date = models.DateField()
    modified_date = models.DateField()
    published_date = models.DateField()

    def __str__(self):
        return self.title