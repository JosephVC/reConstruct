from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponseRedirect

from userprofiles.models import Profile, Project
from wasteprocessors.models import WasteProcessor, MaterialType, Waste, WasteType
from wasteprocessors.forms import WasteForm, SearchFilterForm

# Create your views here.

def salvage_companies_list(request):
    salvage_companies = get_list_or_404(WasteProcessor)
    context = {'salvage_companies': salvage_companies}
    return render(request, 'salvagecompanies.html', context)
# you should move material search into it's own app
def material_search_view(request, project_slug):
    profile = get_object_or_404(Profile, pk=request.user.id)
    project = get_object_or_404(Project, project_slug=project_slug)
    if request.method == 'POST':
        waste = Waste(project=project)
        form = WasteForm(request.POST, instance=waste)
        if form.is_valid():
            waste = form.save()
            return HttpResponseRedirect(
                '/material-search/results/{}/'.format(waste.id)
                )
    else:
        form = WasteForm()
    context = {'profile': profile, 'project': project, 'form': form}
    return render(request, 'materialsearch.html', context)

def material_search_results(request, waste_id):
    waste = get_object_or_404(Waste, pk=waste_id)
    material_processors = WasteProcessor.objects.filter(
        materials_accepted=waste.material_type)
    material_processors = material_processors.filter(
        waste_types_accepted=waste.waste_type)
    # add checkbox form for additional filtering
    if request.method == 'POST':
        form = SearchFilterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['will_purchase']:
                material_processors = material_processors.filter(
                    will_purchase=True)
            if form.cleaned_data['accepts_donations']:
                material_processors = material_processors.filter(
                    accepts_donations=True)
            if form.cleaned_data['will_pick_up']:
                material_processors = material_processors.filter(
                    will_pick_up=True)
            # no need to redirect, rather just render the page with the new
            # search filters
    else:
        form = SearchFilterForm()
    context = {'profile': waste.project.profile,
               'project': waste.project,
               'material_type': waste.material_type,
               'waste_type': waste.waste_type,
               'material_processors': material_processors,
               'form': form,
    }
    return render(request, 'materialsearchresults.html', context)
