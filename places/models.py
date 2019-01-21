from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    country = models.CharField(max_length=256)
    image = models.ImageField(upload_to='places_images/')
    def __str__(self):
        return self.name

class Rate(models.Model):
    rate = models.IntegerField(default=0)
    review = models.CharField(max_length=300)
    place = models.ForeignKey('Place')

    @property
    def des_rates(self):
        return 'تقييم المكان بناءا علي رأي الزائر'

    def __str__(self):
        return '{} - {}'.format(self.rate, self.review)
