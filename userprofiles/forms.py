from django.forms import ModelForm
from userprofiles.models import Profile, Project

# Create a class for the User Profile
class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['user_type', 'company']

#  Create a form for the Project model
class ProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = ['project', 'project_type', 'address']


