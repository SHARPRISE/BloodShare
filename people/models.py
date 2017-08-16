from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

BLOOD_TYPES = (
    ('1', 'A+'),
    ('2', 'A-'),
    ('3', 'B+'),
    ('4', 'B-'),
    ('5', 'O+'),
    ('6', 'O-'),
    ('7', 'AB+'),
    ('8', 'AB-')
)

class User(AbstractUser):
    name = models.CharField(max_length=255)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES, help_text='Your Blood Type')
    phone = models.CharField(max_length=255)

    REQUIRED_FIELDS = ['email', 'name', 'blood_type', 'phone']

    def __str__(self):
        return "%s" % self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.name

    def get_blood_type(self):
        "get the user's blood Type"
        return self.blood_type

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

User._meta.get_field('email')._unique = True
