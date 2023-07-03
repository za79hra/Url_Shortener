from django.db import models
from django.contrib.auth.models import User


class LinkShortenerModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    orginal_url = models.URLField(max_length=1000, null=False, blank=False)
    short_url = models.CharField(max_length=50, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    url_viewed = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.short_url
    
    def get_absolute_url(self):
        return self.orginal_url


  
