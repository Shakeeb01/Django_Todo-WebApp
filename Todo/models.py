from django.db import models



class Todo(models.Model):
    STATUS_CHOICES = [
        ('Completed', 'Completed'),
        ('Inprogress', 'Inprogress'),
        ('Incomplete', 'Incomplete'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Inprogress')


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
