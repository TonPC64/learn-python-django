from django.db import models

class Post(models.Model):
    text = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='posts', null=False, blank=False)
    user = models.ForeignKey('auth.User', null=False, blank=False, on_delete=models.CASCADE)
    created = models.TimeField(auto_now=True)
