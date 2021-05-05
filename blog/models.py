from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.


"""models.Model means that the Post is a Django Model, 
so Django knows that it should be saved in the database.
"""
class Post(models.Model):  # this line defines a model its an object
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
