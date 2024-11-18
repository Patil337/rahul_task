from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="clients")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="projects")
    users = models.ManyToManyField(User, related_name="projects")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_projects")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
