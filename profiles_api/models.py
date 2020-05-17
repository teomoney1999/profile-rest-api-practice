from django.db import models

"""All the functionality from Django default user"""
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# class UserProfileManager(BaseUserManager):
#     """Manager for user profile"""
#
# 	def

class UserProfileManager(BaseUserManager):
	"""Manager for user profile"""

	def create_user(self, email, name, password=None):
		"""Create a new user profile"""
		if not email:
			raise ValueError('User must have an email')
		user = self.model(email, name)
		user.set_password(password)
		user.save(self._db)
		return user

	def create_superuser(self, email, name, password):
		user = self.create_superuser(email, name, password)

		user.is_superuser = True
		user.is_staff = True
		user.save(self._db)

		return user



# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database Model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    # Permission 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self): 
        """Retrive full name of user"""
        return self.name
    
    def __str__(self): 
        return self.email
