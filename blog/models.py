from django.db import models
from telegram_bot.g_model import TimeStampMixin
from accounts.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Blog(TimeStampMixin):
    topic = models.CharField(max_length=64)
    title = models.CharField(max_length=128)    
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def clean(self):
        super().clean()
        if self.author.role != User.RoleChoices.AUTHOR:
            raise ValidationError({'author': 'User must have the role of AUTHOR to be assigned as a blog author.'})

    
    
class Comment(TimeStampMixin):
    comment = models.CharField(max_length=512)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)