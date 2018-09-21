from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Configuration(models.Model):
    trigger = models.BooleanField(default=False, null=False)
    end_point = models.URLField(blank=False, null=False)
    token = models.CharField(max_length=50, blank=False, null=False)
    default = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.end_point

    def save(self, *args, **kwargs):
        if(self.default == True):
            self.__class__.objects.filter(~Q(id=self.id)).update(default=False)
        super(Configuration, self).save(*args, **kwargs)

class User(AbstractBaseUser):
    username = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self._get_unique_username()

        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email