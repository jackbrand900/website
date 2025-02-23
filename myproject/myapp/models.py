from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    published_date = models.DateField()

    class Meta:
        unique_together = ('title', 'author')

    def __str__(self):
        return self.title
