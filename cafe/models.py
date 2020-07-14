from django.db import models

# Create your models here.
class editPost(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

class comment(models.Model):
    comment = models.TextField()