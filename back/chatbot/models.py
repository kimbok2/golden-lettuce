from django.db import models

# Create your models here.

class Conversation(models.Model):
    user_message = models.TextField()
    system_message = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)