from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils.text import slugify

from .forms import ProfileForm, ProjectForm

from userprofiles.models import Profile, Project

# Create your views here.

# View for ProfileForm
def create_profile_view(request):
	if request.method =='POST':
		# create a new profile for the logged in user
		profile = Profile(user=request.user)
		form = ProfileForm(request.POST, instance=profile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/profile/new-project/')
	else:
		form = ProfileForm()
	return render(request, 'profile.html', {'form': form})

def create_project_view(request):
	# get the user's profile
	profile = get_object_or_404(Profile, pk=request.user.id)
	if request.method == 'POST':
		# create a new project for this profile
		project = Project(profile=profile)
		form = ProjectForm(request.POST, instance=project)
		if form.is_valid():
			# generate project slug from project name
			project.project_slug = slugify(form.cleaned_data['project'])
			project.save()
			form.save()
			return HttpResponseRedirect('/material-search/')
	else:
		form =  ProjectForm()
	return render(request, 'project.html', {'form': form})

