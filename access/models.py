from django.db import models

from users.models import User


class AccessManager(models.Manager):
    
    def create_access(self, user_id: str, title: str, username: str, password: str, url: str, notes: str):
        if not user_id:
            raise ValueError('User ID must be provided')
        if not title:
            raise ValueError('Title must be provided')
        if not password:
            raise ValueError('Password must be provided')
        
        access = self.models(user_id=user_id)
        access.title = title
        access.username = username
        access.password = password
        access.url = url
        access.notes = notes
        access.save()

        return access
    

class Access(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Title', max_length=255)
    username = models.CharField(verbose_name='Username', max_length=255)
    password = models.CharField(verbose_name='Password', max_length=255)
    url = models.URLField(verbose_name='URL')
    notes = models.TextField(verbose_name='Notes', max_length=255)

    objects = AccessManager()

    REQUIRED_FIELDS = ['user_id', 'title', 'password']
