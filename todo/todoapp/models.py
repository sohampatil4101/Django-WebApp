from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    desc = models.TextField()
    # date = models.DateField()

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.TextField()
    task = models.TextField()
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.task


