from django.db import models

# Create your models here.
# Models are Python classes that represent database tables.

# Example: If you want to store chat conversations:
"""
class ChatMessage(models.Model):
    user_message = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Chat at {self.timestamp}"
"""

# After creating a model:
# 1. Run: python manage.py makemigrations
# 2. Run: python manage.py migrate
# 3. Register in admin.py if you want to view/edit in admin panel
