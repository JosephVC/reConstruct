from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponseRedirect

from userprofiles.models import Profile, Project
from wasteprocessors.models import WasteProcessor, MaterialType, Waste, WasteType
from wasteprocessors.forms import WasteForm

# Create your views here.

def salvage_companies_list(request):
    salvage_companies = get_list_or_404(WasteProcessor)
    context = {'salvage_companies': salvage_companies}
    return render(request, 'salvagecompanies.html', context)

def material_search_view(request, project_slug):
    profile = get_object_or_404(Profile, pk=request.user.id)
    project = get_object_or_404(Project, project_slug=project_slug)
    if request.method == 'POST':
        waste = Waste(project=project)
        form = WasteForm(request.POST, instance=waste)
        if form.is_valid():
            waste = form.save()
            return HttpResponseRedirect('/material-search/results/{}/'.format(waste.id))
    else:
        form = WasteForm()
    context = {'profile': profile, 'project': project, 'form': form}
    return render(request, 'materialsearch.html', context)

def material_search_results(request, waste_id):
    waste = get_object_or_404(Waste, pk=waste_id)
    profile = get_object_or_404(Profile, pk=request.user.id)
    project = get_object_or_404(Project, pk=waste.project.id)
    material_type = get_object_or_404(MaterialType, pk=waste.material_type.id)
    waste_type = get_object_or_404(WasteType, pk=waste.waste_type.id)
    material_processors = WasteProcessor.objects.filter(materials_accepted=material_type)
    material_processors = material_processors.filter(waste_types_accepted=waste_type)
    context = {'profile': profile,
               'project': project,
               'material_type': material_type,
               'material_processors': material_processors
    }
    return render(request, 'materialsearchresults.html', context)
