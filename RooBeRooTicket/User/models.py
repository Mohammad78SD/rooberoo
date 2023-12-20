from django.db import models
from django.core.validators import RegexValidator
from django_jalali.db import models as jmodels


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone_number = models.CharField(
            max_length=15,
            validators=[
                RegexValidator(
                    regex=r"^\+\d{1,3}\d{3}\d{3}\d{4}$",
                    message="Phone number must be in the format +XXX-XXX-XXXX.",
                )
            ],
            unique=True,
        )
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=255)
    date_of_birth = jmodels.jDateTimeField()
    # membership = models.ManyToManyField('Membership', through='UserMembership')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)