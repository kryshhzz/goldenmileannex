from django.db import models
from django.core.validators import RegexValidator
import datetime
from django.utils import timezone
from django.core.validators import MinValueValidator

# Create your models here.

class keep_me_interested(models.Model):
    name = models.CharField(blank=False, max_length=255)
    phone_number = models.CharField(validators=[RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )], max_length=17, blank=True, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name+' - '+self.phone_number


class enquiry(models.Model):
    name = models.CharField(blank=False, max_length=255)
    phone_number = models.CharField(validators=[RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )], max_length=17, blank=True, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=False)

    def __str__(self):
        return self.name+' - '+self.phone_number


class plan_a_visit(models.Model):
    name = models.CharField(blank=False, max_length=255)
    phone_number = models.CharField(validators=[RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )], max_length=17, blank=True, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    preferred_date = models.DateField(default=datetime.datetime.now() + datetime.timedelta(days=1),validators=[MinValueValidator(timezone.now().date())], blank=False, null=False)
    preferred_time = models.TimeField(default=datetime.datetime.now().time(),validators=[MinValueValidator(timezone.now().time())], blank=False, null=False)

    def __str__(self):
        return self.name+' - '+self.phone_number
