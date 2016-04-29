from django.forms import ModelForm
from wasteprocessors.models import Waste

class WasteForm(ModelForm):

    class Meta:
        model = Waste
        fields = '__all__'