from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    BLOG_ACTIVE_CHOICES = (
        ('ac', 'Active'),
        ('nac', "Not active"),
    )

    blog_active = models.CharField(max_length=4, choices=BLOG_ACTIVE_CHOICES)
