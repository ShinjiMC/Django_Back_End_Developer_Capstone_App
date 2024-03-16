from django.db import models
from django.utils import timezone
# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255, default='')
    number_of_guests = models.IntegerField(default=6)
    booking_date =models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Booking Records'

    def __str__(self) -> str:
        return f'{self.name} for {self.number_of_guests} guests on {self.booking_date}'


# Add code to create Menu model
class Menu(models.Model):
    title = models.CharField(max_length=255, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    inventory = models.IntegerField(default=5)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu Items'

    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'