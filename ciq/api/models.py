from django.db import models
from django.db.models import Count
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
 
 
class Post(models.Model):
    title = models.CharField(max_length=100)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE,related_name="posts")
    views = models.PositiveIntegerField(default=1)
    reviews = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f'{self.title}'
    
    @property
    def author(self):
        return f'{self.author_name.first_name}{self.author_name.last_name}'