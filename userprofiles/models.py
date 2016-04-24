from django.db import models

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

class Waste(models.Model):
    project = models.ForeignKey(Project)
    description = models.CharField(max_length=128)
    waste_type = models.ForeignKey(WasteType)
    material = models.ForeignKey(Material)

    def __str__(self):
        return self.description