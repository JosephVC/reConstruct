from django import forms
from wasteprocessors.models import Waste

class WasteForm(forms.ModelForm):

    class Meta:
        model = Waste
        fields = ['waste_type', 'material_type']

class SearchFilterForm(forms.Form):
    will_purchase = forms.BooleanField(label='Will purchase', required=False)
    accepts_donations = forms.BooleanField(label='Accepts donations', required=False)
    will_pick_up = forms.BooleanField(label='Onsite pickup', required=False)