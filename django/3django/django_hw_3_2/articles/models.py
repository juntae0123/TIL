from django.db import models

class article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=15)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title