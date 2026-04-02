from django.db import models

class FaultReport(models.Model):
    CATEGORY_CHOICES = [
        ('water', 'Water/Burst Pipe'),
        ('elec', 'Electricity Outage'),
        ('road', 'Pothole/Roads'),
        ('lights', 'Streetlights'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending (Red)'),
        ('assigned', 'Assigned (Orange)'),
        ('resolved', 'Resolved (Green)'),
    ]

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='fault_photos/', null=True, blank=True)
    location_lat = models.FloatField(null=True, blank=True)
    location_lng = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_category_display()} - {self.title}"