from django.shortcuts import render, get_list_or_404

from wasteprocessors.models import WasteProcessor

# Create your views here.

def salvage_companies_list(request):
    salvage_companies = get_list_or_404(WasteProcessor)
    context = {'salvage_companies': salvage_companies}
    return render(request, 'salvagecompanies.html', context)