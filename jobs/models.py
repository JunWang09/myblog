from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    summary = models.TextField()
    body = models.TextField(default='More details are coming soon!')

    def __str__(self):
        return self.title
