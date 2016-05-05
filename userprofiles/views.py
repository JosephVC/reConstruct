from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils.text import slugify

from .forms import ProfileForm, ProjectForm

from userprofiles.models import Profile, Project

# Create your views here.

def home_view(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/profile/')
	else:
		return render(request, 'home.html')

def profile_view(request):
	profile, created = Profile.objects.get_or_create(user=request.user)
	if created:
		return HttpResponseRedirect('/profile/edit/')
	else:
		return render(request, 'profile.html', {'profile': profile})

def edit_profile_view(request):
	if request.method =='POST':
		profile = get_object_or_404(Profile, user=request.user)
		form = ProfileForm(request.POST, instance=profile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/new-project/')
	else:
		form = ProfileForm()
	return render(request, 'editprofile.html', {'form': form})

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
			return HttpResponseRedirect(
				'/material-search/project/{}/'.format(
				project.project_slug))
	else:
		form =  ProjectForm()
	return render(request, 'project.html', {'form': form})

