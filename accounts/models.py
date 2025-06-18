# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from telegram_bot.g_model import TimeStampMixin


class User(AbstractUser, TimeStampMixin):
    class RoleChoices(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        EDITOR = 'editor', 'Editor'
        AUTHOR = 'author', 'Author'
        VISITOR = 'visitor', 'Visitor'  
    
    email = models.EmailField(
        _('email address'),
        unique=True,        # Prevent duplicate emails
        blank=False,         # Make field required
        null=False,
        error_messages={
            'unique': _("A user with that email already exists."),
        }
    )     
  
    role = models.CharField(max_length=20, choices=RoleChoices, default=RoleChoices.VISITOR)
    
    
    
    def __str__(self):
        return self.email
    
    def user_role(self):
        return self.role