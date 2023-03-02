from django.db import models
from datetime import datetime
from taggit.managers import TaggableManager 

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images/")
    description=models.TextField()
    description_steps= models.TextField(blank=True)
    keywords = models.CharField(max_length=200)
    tags = TaggableManager()
    author=models.CharField(max_length=50)
    created_at=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title


