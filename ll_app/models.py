from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from djmoney.models.fields import MoneyField


# Create your models here.
class Zipcode(models.Model):
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return self.zipcode


class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    profile_zipcode = models.ForeignKey(Zipcode, verbose_name='Preferred Zipcode', null=True, on_delete=models.PROTECT)


    def __str__(self):
        return str(self.user)


class ListingType(models.Model):
    name = models.CharField(max_length=20)
    parent = models.ForeignKey("self", null=True, blank=True, related_name='subcat', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Listing(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    listing_zipcode = models.ForeignKey(Zipcode, on_delete=models.PROTECT)
    address = models.CharField(max_length=40)
    sqft = models.IntegerField()
    category = models.ForeignKey(ListingType, on_delete=models.PROTECT)
    title = models.CharField(max_length=40)
    price = MoneyField(max_digits=12, decimal_places=2, default_currency='USD')
    summary = models.TextField()
    photo = models.ImageField(upload_to="listing_photos", null=True, blank=True, verbose_name="Listing Photo")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    @property
    def photo_url(self):
        if self.photo:
            return self.photo.url
        return "/media/listing_photos/classifieds-default.jpg"


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get("created")
    instance = kwargs.get("instance")
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender='auth.User')
def create_token(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Token.objects.create(user=instance)
