from django.db import models

# Create your models here.
class libraries_book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.TextField()
    pubdate = models.DateField()
    price = models.IntegerField()
    adult = models.BooleanField()

    def __str__(self):
        return self.title  