from django.db import models
from django_jalali.db import models as jmodels
from User.models import User
import segno
import uuid



# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    # banner = models.ImageField(upload_to='images/')
    # photos_gallery
    # video_teaser = models.FileField(upload_to='videos/')
    
    class Meta:
        verbose_name = "اجرا"
    def __str__(self) -> str:
        return self.title


class Sans(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    free_capacity = models.IntegerField()
    min_ticket = models.IntegerField()
    max_ticket = models.IntegerField()
    start_sale_date = jmodels.jDateTimeField()
    end_sale_date = jmodels.jDateTimeField()
    datetime = jmodels.jDateTimeField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.event.title + " سانس " + self.datetime.strftime("%Y-%m-%d %H:%M"))
    class Meta:
        verbose_name = "سانس"
    
class Review(models.Model):
    review_text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rooydad = models.ForeignKey(Event, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "نظرات"
    
    def __str__(self) -> str:
        return (self.user.name + self.rooydad.title)

def generate_QR_code(ticketid):
    qrcode = segno.make_qr(ticketid)
    return qrcode

class Ticket(models.Model):
    ticketid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sans = models.ForeignKey(Sans, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "بلیت"
    quantity = models.IntegerField()
    QR_code = generate_QR_code(str(ticketid))
    
    def __str__(self) -> str:
        return ("بلیت (" + self.user.name + ") - اجرا (" + self.sans.event.title + ") - سانس (" + self.sans.datetime.strftime("%Y-%m-%d %H:%M:%S") + ")")
    