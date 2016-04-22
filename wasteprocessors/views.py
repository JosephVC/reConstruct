from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponseRedirect

from wasteprocessors.models import WasteProcessor, Profile
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
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = WasteForm()
    context = {'profile': profile, 'form': form}
    return render(request, 'materialsearch.html', context)
