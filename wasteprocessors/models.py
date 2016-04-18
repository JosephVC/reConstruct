from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserType(models.Model):
    user_type = models.CharField(max_length=128) # contractor, home owner, salvage company etc.

    def __str__(self):
        return self.user_type

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.ForeignKey(UserType)
    company = models.CharField(max_length=128)

    def __str__(self):
        return self.user.username

class ProjectType(models.Model):
    project_type = models.CharField(max_length=128) # new construction, remodel, commercial construction etc.

    def __str__(self):
        return self.project_type

class Project(models.Model):
    profile = models.ForeignKey(Profile, related_name='projects')
    project = models.CharField(max_length=128)
    project_type = models.ForeignKey(ProjectType)
    address = models.CharField(max_length=128)

    def __str__(self):
        return self.project

class MaterialType(models.Model):
    material_type = models.CharField(max_length=128) # wood, brick, reusable building materials etc.
    description = models.TextField(blank=True)
    special_considerations = models.TextField(blank=True)

    def __str__(self):
        return self.material_type

class Material(models.Model):
    material = models.CharField(max_length=128) # pressure treated lumber, cedar siding shingles etc.
    material_type = models.ForeignKey(MaterialType)
    description = models.TextField(blank=True)
    special_considerations = models.TextField(blank=True)

    def __str__(self):
        return self.material

class WasteType(models.Model):
    waste_type = models.CharField(max_length=128) # salvage, scrap, surplus etc.

    def __str__(self):
        return self.waste_type

class Waste(models.Model):
    project = models.ForeignKey(Project)
    description = models.CharField(max_length=128)
    waste_type = models.ForeignKey(WasteType)
    material = models.ForeignKey(Material)

    def __str__(self):
        return self.description

class WasteProcessor(models.Model):
    company = models.CharField(max_length=128)
    description = models.TextField()
    website = models.URLField()
    phone = models.CharField(max_length=15)
    business_hours = models.TextField(blank=True)
    email = models.EmailField()
    address = models.CharField(max_length=128)
    materials_accepted = models.ManyToManyField(Material, related_name='materials')
    will_pick_up = models.BooleanField()
    will_purchase = models.BooleanField()
    accepts_donations = models.BooleanField()

    def __str__(self):
        return self.company
