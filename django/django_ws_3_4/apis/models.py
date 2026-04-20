from django.db import models


class apiInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    api_url = models.URLField(max_length=200)
    documentation_url = models.URLField(max_length=200)
    auth_required = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name