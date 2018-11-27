from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=258)
    publish_date = models.DateField()
    owner = models.CharField(max_length=200)
    body = models.TextField()
    summary = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
