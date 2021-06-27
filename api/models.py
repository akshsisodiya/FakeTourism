from django.db import models

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField()
    image2 = models.ImageField()
    ratings = models.IntegerField()
    action_button_link = models.URLField()
    more_detail_link = models.URLField()

class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField()
    image2 = models.ImageField()
    ratings = models.IntegerField()
    action_button_link = models.URLField()
    more_detail_link = models.URLField()


CHOICE = (
    ('male', 'male'),
    ('female','female'),
    ('both, both is good', 'both'),
)
class Pedophile(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    gender_preference = models.Choices(CHOICE)

class Location(models.Model):
    name = models.CharField(max_length=250)
    googleMapLink = models.URLField()
    image1 = models.ImageField()
    image2 = models.ImageField()
    # hot_milfs_in_area = models.slutField()
    hotels_in_area = models.ManyToManyField('Hotel', on_delete=models.CASCADE)
    restaurants_in_area = models.ManyToManyField('Restaurant', on_delete=models.CASCADE)
    pedophiles_in_area = models.ManyToManyField('Pedophile', on_delete=models.CASCADE)