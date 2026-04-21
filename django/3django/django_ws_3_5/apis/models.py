from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class APIInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    api_url = models.URLField(MinLengthValidator(15), MaxLengthValidator(60))
    documentation_url = models.URLField()
    auth_required = models.BooleanField()
    additional_info = models.TextField(blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
