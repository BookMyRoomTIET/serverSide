import uuid
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from hostel.models import *

class UserManager(BaseUserManager):
    """
    Custom User Manager to use email as unique identifier
    """

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Email address required")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(email, name, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    """
    Custom User model
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    email = models.EmailField(max_length=255, unique=True, verbose_name="email address",editable=True)
    registration_id = models.IntegerField(unique=True,null=True,editable=True)
    hostel = models.ForeignKey(hostelInformationModel, on_delete=models.CASCADE, default=-1,editable=True)
    phone = models.CharField(max_length=100, unique=True,editable=True)
    name = models.CharField("Name", max_length=20,editable=True)
    is_warden = models.BooleanField(default=False,editable=True)
    is_staff = models.BooleanField(default=False,editable=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name",]
    

    objects = UserManager()

    def __str__(self):
        return f"{self.name}"
    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

class Warden(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    designation = models.CharField(max_length=100,editable=True)

    def __str__(self):
        return self.user.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    grad_year = models.IntegerField(blank=True,null=True,editable=True)
    branch = models.CharField(max_length=10,blank=True,null=True,editable=True)
    sex = models.CharField(max_length=10,editable=True,null=True)
    fee_paid = models.BooleanField(default=False,editable=True)

    def __str__(self):
        return self.user.name