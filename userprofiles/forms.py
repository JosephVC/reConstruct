from django.forms import ModelForm
from userprofiles.models import UserType, Profile, ProjectType, Project, Waste

#  creating the form class
class UserTypeForm(ModelForm):
	class Meta:
		model = UserType
		fields = ['user_type']

#  creating a form to add a user
form = UserTypeForm()

# creating a form to change an existing user
user = UserType.objects.get(pk=1)
form = UserTypeForm(instance=user)

# Create a class for the User Profile
class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['user', 'user_type', 'company']

#  create a form to add a user's profile 
form = ProfileForm()

#  Create a form to change an existing profile
profile = Profile.objects.get(pk=1)

# Create a form for the ProjectType model
class ProjectTypeForm(ModelForm):
	class Meta: 
		model = ProjectType
		fields = ['project_type']

#  create a form to add a user's project type
form = ProjectTypeForm()

#  Create a form to change an existing project type
profile = Profile.objects.get(pk=1)

#  Create a form for the Project model
class ProjectForm(ModelForm):
	class Meta:
		model = ProjectType
		fields = ['profile', 'project', 'project_type', 'address']

#  Create a form to add a user's project type
form = ProjectForm

#  Create a form to change an existing project type
profile = Profile.objects.get(pk=1)

#  Create a form for the Waste model
class WasteForm(ModelForm):
	class Meta:
		model = Waste
		fields = ['project', 'description','waste_type','material']

#  Create a form to add what sort of waste a user is disposing of
form = WasteForm

#  Create a form to change the existing waste form
profile = Profile.objects.get(pk=1)