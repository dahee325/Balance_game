from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    A = models.CharField(max_length=100)
    B = models.CharField(max_length=100)


class Comment(models.Model):
    AB = models.CharField(max_length=100, choices=[('A', 'A'), ('B', 'B')], default='1')
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)