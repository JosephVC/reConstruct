from django.shortcuts import render
from django.http imort HttpResponseRedirect

from .forms import UserTypeForm, ProfileForm, ProjectTypeForm, ProjectForm, WasteForm

# Create your views here.

# UserTypeForm
def get_user_type(request):
	if request.method =='POST':
		form = UserTypeForm(request.POST)

		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form = UserTypeForm()

	return render(request, 'user_type.html', {'form': form})


# View for ProfileForm
def get_profile(request):
	if request.method =='POST':
		form = ProfileForm(request.POST)

		if form.is_valid():
			return HttpResponseRedirect('/thanks/')

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
