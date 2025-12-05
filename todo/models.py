from django.db import models

# Create your models here.
class Todo(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    task=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.task} Id:{self.id}"