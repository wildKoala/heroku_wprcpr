from django.db import models

# Create your models here.
class ClassBox(models.Model):
    class_name = models.CharField(max_length=8)
    #department = models.CharField(max_length=6)
    link = models.URLField()

    def __str__(self):
        return self.class_name
