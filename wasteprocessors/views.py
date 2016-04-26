from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponseRedirect

from wasteprocessors.models import WasteProcessor, Profile, MaterialType, Project
from wasteprocessors.forms import WasteForm

# Create your views here.

def salvage_companies_list(request):
    salvage_companies = get_list_or_404(WasteProcessor)
    context = {'salvage_companies': salvage_companies}
    return render(request, 'salvagecompanies.html', context)

def material_search_view(request):
    profile = get_object_or_404(Profile, pk=request.user.id)
    if request.method == 'POST':
        form = WasteForm(request.POST)
        project = Project.objects.get(pk=request.POST['project'])
        material_type = MaterialType.objects.get(pk=request.POST['material_type'])
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                '/material-search/{}/{}/'.format(
                project.project_slug, material_type.material_slug))
    else:
        form = WasteForm()
    context = {'profile': profile, 'form': form}
    return render(request, 'materialsearch.html', context)

def material_search_results(request, project_slug, material_slug):
    profile = get_object_or_404(Profile, pk=request.user.id)
    project = get_object_or_404(Project, project_slug=project_slug)
    material_type = get_object_or_404(MaterialType, material_slug=material_slug)
    material_processors = WasteProcessor.objects.filter(materials_accepted=material_type)
    context = {'profile': profile,
               'project': project,
               'material_type': material_type,
               'material_processors': material_processors
    }
    return render(request, 'materialsearchresults.html', context)
