from django.db import models

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    phone = models.TextField(max_length=50)
    image_path = models.TextField()
    punch_status = models.TextField()
    user_type = models.TextField()

    def __str__(self):
        return self.name
