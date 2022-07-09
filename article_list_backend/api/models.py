from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/4.0/topics/db/models/

#step-3
class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.TextField()
    # add app name under INSTALLED_APPS in project's settings.py to be able to makemigrations

    # #step-5b (first way)
    # def __str__(self): # https://www.pythontutorial.net/python-oop/python-__str__/
    #     return self.title
    #     # now you can see the title display on the admin interface page