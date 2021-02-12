from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def get_absolute_url(self):
        return f"products/{self.id}"
    
