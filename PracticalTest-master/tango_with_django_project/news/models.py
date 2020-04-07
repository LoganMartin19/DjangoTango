from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class NewsArticle(models.Model):
    headline = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    published = models.DateTimeField('date published')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.headline

# Create your models here.
