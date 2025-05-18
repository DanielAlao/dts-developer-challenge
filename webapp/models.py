from django.db import models

# Create your models here.

# DJANGO ORM


class Task(models.Model):
    STATUS = [
        ('Started', 'Started'),
        ('In progress', 'In progress'),
        ('Done', 'Done')
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=STATUS, default='Started')
    due_date = models.DateField()

    def __str__(self):
        return self.title
