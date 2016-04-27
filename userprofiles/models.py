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
    user_type = models.ForeignKey(UserType)
    company = models.CharField(max_length=128)

    def __str__(self):
        return self.user.username

class ProjectType(models.Model):
    """A model for storing categories of construction projects such as
    new construction, commercial construction, residential construction,
    remodel, home owner project etc."""
    project_type = models.CharField(max_length=128)

    def __str__(self):
        return self.project_type

class Project(models.Model):
    """A model for storing a specific construction project, registered
    by a user along with its associated data."""
    profile = models.ForeignKey(Profile, related_name='projects')
    project = models.CharField(max_length=128)
    project_slug = models.SlugField()
    project_type = models.ForeignKey(ProjectType)
    address = models.CharField(max_length=128)

    def __str__(self):
        return self.project