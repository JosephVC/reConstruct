import geocoder

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

class Location(models.Model):
    """Abstract base model for other location based models. Uses geocoder
    package to retrieve latitude and longitude coordinates from stored
    address data for use in mapping search feature."""
    address = models.CharField(max_length=128, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        abstract = True

    def get_lat_and_lng(self):
        """This method converts an address to latitude and longitude
        coordinates and saves these values to model instance. Use the
        django shell to call method on new waste processors afers entering
        in their address through the admin. Call on new projects when they
        are created in create_project_view."""
        geocode_result = geocoder.osm(self.address)
        latlng = geocode_result.latlng
        try:
            self.latitude = latlng[0]
            self.longitude = latlng[1]
        except IndexError:
            self.latitude = None
            self.longitude = None
        self.save()

class Project(Location):
    """A model for storing a specific construction project, registered
    by a user along with its associated data."""
    profile = models.ForeignKey(Profile, related_name='projects')
    project = models.CharField(max_length=128, blank=True)
    project_slug = models.SlugField(blank=True)
    project_type = models.ForeignKey(ProjectType, null=True)
    # address = models.CharField(max_length=128, blank=True)

    # def get_lat_and_lng(self):
    #     geocode_result = geocoder.osm(self.address)
    #     latlng = geocode_result.latlng
    #     try:
    #         self.latitude = latlng[0]
    #         self.longitude = latlng[1]
    #     except IndexError:
    #         self.latitude = None
    #         self.longitude = None


    def __str__(self):
        return self.project