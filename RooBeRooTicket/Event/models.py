from django.db import models
from django_jalali.db import models as jmodels
from User.models import User


# Create your models here.
class rooydad(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    # banner = models.ImageField(upload_to='images/')
    # photos_gallery
    # video_teaser = models.FileField(upload_to='videos/')

class ejra(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    free_capacity = models.IntegerField()
    min_ticket = models.IntegerField()
    max_ticket = models.IntegerField()
    start_sale_date = jmodels.jDateTimeField()
    end_sale_date = jmodels.jDateTimeField()
    description = models.TextField()
    rooydad = models.ManyToManyField(rooydad)
    
class sans(models.Model):
    date = jmodels.jDateTimeField()
    ejra = models.ManyToManyField(ejra)
    
class review(models.Model):
    review_text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rooydad = models.ForeignKey(rooydad, on_delete=models.CASCADE)
    

    