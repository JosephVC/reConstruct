import googlemaps

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserType(models.Model):
    """A model for storing the type of user, such as construction business,
    home owner, salvage company, recycling company etc. This allows for
    certain features of our app to be targeted to specific kinds of users."""
    user_type = models.CharField(max_length=128)

    def __str__(self):
        return self.user_type

class Profile(models.Model):
    """A model for storing data related to specific users."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.ForeignKey(UserType, null=True)
    company = models.CharField(max_length=128, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.user.username

class ProjectType(models.Model):
    """A model for storing categories of construction projects such as
    new construction, commercial construction, residential construction,
    remodel, home owner project etc."""
    project_type = models.CharField(max_length=128)

    def __str__(self):
        return self.project_type

# refactor to use Place superclass for Project and WasteProcessor? so you dont
# repeat code
class Project(models.Model):
    """A model for storing a specific construction project, registered
    by a user along with its associated data."""
    profile = models.ForeignKey(Profile, related_name='projects')
    project = models.CharField(max_length=128, blank=True)
    project_slug = models.SlugField(blank=True)
    project_type = models.ForeignKey(ProjectType, null=True)
    address = models.CharField(max_length=128, blank=True)

    def get_latitude(self):
        gmaps = googlemaps.Client(key='AIzaSyBUpzrFpwR4gGj_MBG2xxyOFsVllJvqKjw')
        # returns a dict of geocoding data
        geocode_result = gmaps.geocode(self.address)
        self.latitude = geocode_result[0]['geometry']['location']['lat']

    def get_longitude(self):
        gmaps = googlemaps.Client(key='AIzaSyBUpzrFpwR4gGj_MBG2xxyOFsVllJvqKjw')
        geocode_result = gmaps.geocode(self.address)
        self.longitude = geocode_result[0]['geometry']['location']['lng']


    def __str__(self):
        return self.project