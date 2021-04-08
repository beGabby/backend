from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.contrib.postgres.fields import ArrayField


class UserManager(BaseUserManager):

    def create_user(self, email, age, interestings, languages, password=None, **extra_fields):
        """Creates and saves a new User"""
        if not email:
            raise ValueError('Users must have email adress')
        user = self.model(email=self.normalize_email(email), **extra_fields, age=age, interestings=interestings, languages=languages)
        
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        age=22
        interestings=['sport', 'play station'] 
        languages=['{"language":"english", "level": "beginner"}','{"language":"german", "level": "native"}']
        """create a new superuser """
        user = self.create_user(email=email, age=age, interestings=interestings, languages=languages, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user



class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=253, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(default=1000)
    languages = ArrayField(ArrayField(models.CharField(max_length=255)))
    #languages = models.JSONField(encoder=None)
    likes = models.IntegerField(default=0)
    #friends = ArrayField(ArrayField(models.CharField(max_length=255)))
    interestings = ArrayField(ArrayField(models.CharField(max_length=255)))


    objects = UserManager()


    USERNAME_FIELD = 'email'




class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

"""
class LanguageAndPerson(models.Model):
    #id osoby klucz obcy 
    #id jezyka klucz obcy
    #level
    
"""


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class NOWA(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title



class Friends(models.Model):
      user_id_one = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_id_one')
      user_ide_two = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_ide_two')
      