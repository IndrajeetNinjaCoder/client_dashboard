from django.db import models

# Create your models here.
class Project(models.Model):
    projectId = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    _from = models.DateField()
    _to = models.DateField()
    work_status = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} for {self.client}"