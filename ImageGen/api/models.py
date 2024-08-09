from django.db import models
from django.utils import timezone


class GeneratedImage(models.Model):
    prompt = models.CharField(max_length=255)
    image_base64 = models.TextField()  # To store the base64 encoded image
    seed = models.CharField(max_length=255)  # Assuming seed is a string; adjust as needed
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Image generated for prompt: {self.prompt}"