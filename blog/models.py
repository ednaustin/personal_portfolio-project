from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    date = models.DateField()
    """image = models.ImageField(upload_to='portfolio/images/')"""
    """url = models.URLField(blank=True)"""
