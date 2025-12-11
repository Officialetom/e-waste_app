from django.db import models

class EWasteItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[
        ('Phone', 'Phone'),
        ('Laptop', 'Laptop'),
        ('Television', 'Television'),
        ('Battery', 'Battery'),
        ('Other', 'Other'),
    ])
    address = models.TextField()
    pickup_date = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Picked Up', 'Picked Up'),
    ], default='Pending')

    def __str__(self):
        return f"{self.name} ({self.category})"
