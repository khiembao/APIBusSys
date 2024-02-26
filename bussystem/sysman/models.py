from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.



# class Article(models.Model):
#     title = models.CharField('Title', max_length=200)
#     text = CKEditor5Field('Text', config_name='extends')

class User(AbstractUser):
    # avatar = CloudinaryField('avatar', null=True)


    def __str__(self):
        return self.email


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Destination(BaseModel):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

class SpecialOccasion(BaseModel):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()

    def __str__(self):
        return self.name

class Bus(BaseModel):
    model = models.CharField(max_length=50, null=False)
    bienso = models.CharField(max_length=100, null=False)
    capacity = models.IntegerField(default=45, null=False)
    image = models.ImageField(upload_to='busses/%Y/%m', null=True)

    def __str__(self):
        return self.model

#
class TripPath(BaseModel):
    departure_destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='departure')
    arrival_destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='arrival')
    price = models.DecimalField(max_digits=8, decimal_places=0)

    class Meta:
        unique_together = ('departure_destination', 'arrival_destination')

    def __str__(self):
        return f"{self.departure_destination} - {self.arrival_destination}"

class Trip(models.Model):
    trip_depart_time = models.DateTimeField(null=True, blank=True)
    trip_arrive_time = models.DateTimeField(null=True, blank=True)
    trip_path = models.ForeignKey(TripPath, null=True, on_delete=models.CASCADE)
    bus = models.OneToOneField(Bus, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.trip_path}, Trip depart at: {self.trip_depart_time}, Trip arrive at: {self.trip_arrive_time}, {self.bus}"

class Seat(models.Model):
    name = models.CharField(max_length=50, null=True)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    @receiver(post_save, sender=Bus)
    def create_seats(sender, instance, created, **kwargs):
        if created:
            for seat in range(0, instance.capacity):
                instance.seat_set.create()
    def __str__(self):
        return f"{self.id}, {self.bus}"
    # @receiver(post_save, sender=Bus)
    # def selected_seat(sender, instance, selected, **kwargs):
    #     if selected:
    #         instance.capacity -= 1
    #         instance.active = False
    #         instance.capacity.save()
class Ticket(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    qr_code = models.CharField(max_length=100, null=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.trip}, {self.seat}"
    class Meta:
        unique_together = ('trip', 'seat')




