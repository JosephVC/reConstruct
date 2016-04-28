from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ProfileForm, ProjectForm

from userprofiles.models import Profile

# Create your views here.

# View for ProfileForm
def create_profile_view(request):
	if request.method =='POST':
		# create a new profile for the logged in user
		profile = Profile(user=request.user)
		form = ProfileForm(request.POST, instance=profile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = ProfileForm()
	return render(request, 'profile.html', {'form': form})

#  View for ProjectTypeForm
def get_project_type(request):
	if request.method =='POST':
		form = ProjectTypeForm(request.POST)

		if form.is_valid():
			return HttpResponseRedirect('/thanks/')

	else:
		form = ProjectTypeForm()

	return render(request, 'project_type.html', {'form': form})

#  View for ProjectForm
def get_project(request):
	if request.method == 'POST':
		form = ProjectForm(request.POST)

		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form =  ProjectForm()
	return render(request, 'project.html', {'form': form})

# View for WasteForm
def get_waste(request):
	if request.method == 'POST':
		form = WasteForm(request.POST)

		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form = WasteForm()
	return render(request, 'waste.html', {'form': form})
