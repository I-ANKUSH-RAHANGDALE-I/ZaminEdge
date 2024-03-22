from django.db import models

class Property(models.Model):
    #sr_no = models.IntegerField(primary_key=True, default=1)
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=300)
    bedrooms = models.PositiveIntegerField(default=1)
    bathrooms = models.PositiveIntegerField(default=1)
    amenities = models.CharField(default=1,max_length=255)
    location = models.CharField(max_length=255, default='Location of property')

class Photo(models.Model):
    property = models.ForeignKey(Property, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_photos')

class Video(models.Model):
    property = models.ForeignKey(Property, related_name='videos', on_delete=models.CASCADE)
    video_url = models.FileField(upload_to='property_videos')

    def __str__(self):
        return self.address


