from django.db import models

class all_blog(models.Model):
    title = models.CharField(max_length =100)
    description = models.TextField()
    date= models.DateField()
