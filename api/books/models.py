from django.db import models

import uuid

# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=165)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)