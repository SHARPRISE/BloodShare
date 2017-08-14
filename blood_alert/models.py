from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse

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

class Alert(models.Model):
    name = models.CharField(max_length=255, default='Name')
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES, help_text='Your Blood Type')
    phone = models.CharField(max_length=255)
    location = models.CharField(max_length=255, help_text='Your location/address')
    date_time_posted = models.DateTimeField(auto_now_add=True, verbose_name='Alert posted on')
    message = models.TextField(max_length=255, help_text='A message')
    resolved = models.BooleanField(default=False)

    def compatible_donor(self):
        if self.blood_type == '1':
            return 'O-, O+, A-, A+ can donate'
        elif self.blood_type == '2':
            return 'O-, A- can donate'
        elif self.blood_type == '3':
            return 'O-, O+, B+, B- can donate'
        elif self.blood_type == '4':
            return 'O-, B- can donate'
        elif self.blood_type == '5':
            return 'O+, O- can donate'
        elif self.blood_type == '6':
            return 'O- can donate'
        elif self.blood_type == '7':
            return 'Everyone can donate'
        elif self.blood_type == '8':
            return 'O-, A-, B-, AB- can donate'
        else:
            return 'Invalid BLood Type, Contact admin'
