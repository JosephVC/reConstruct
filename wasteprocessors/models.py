import geocoder

from django.db import models

from userprofiles.models import Location, Project
from wasteprocessors.salvage_companies import all_companies


class MaterialType(models.Model):
    """A model for storing broad categories of building materials such as
    wood, brick, concrete, reusable building materials etc."""
    material_type = models.CharField(max_length=128)
    material_slug = models.SlugField()
    description = models.TextField(blank=True)
    special_considerations = models.TextField(blank=True)

    def __str__(self):
        return self.material_type

class WasteType(models.Model):
    """A model for storing various categories of construction waste such
    as salvage, scrap, surplus etc."""
    waste_type = models.CharField(max_length=128) # salvage, scrap, surplus etc.

    def __str__(self):
        return self.waste_type

class Waste(models.Model):
    """A specific waste item generated by a contractor or home owner that
    they wish to recycle, sell or donate for reuse."""
    project = models.ForeignKey(Project)
    waste_type = models.ForeignKey(WasteType)
    material_type = models.ForeignKey(MaterialType, null=True)

    def __str__(self):
        return self.material_type.material_type

class WasteProcessor(Location):
    """A model for storing data related to a specific construction waste
    processing business or service."""
    company = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    business_hours = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    # address = models.CharField(max_length=128, blank=True)
    materials_accepted = models.ManyToManyField(MaterialType, related_name='material_types')
    will_pick_up = models.BooleanField(default=False)
    will_purchase = models.BooleanField(default=False)
    accepts_donations = models.BooleanField(default=False)
    paid_service = models.BooleanField(default=False)
    waste_types_accepted = models.ManyToManyField(WasteType, related_name='waste_types', blank=True)

    def __str__(self):
        return self.company

    @classmethod
    def load_waste_processor_data(cls, all_companies):
        """A method for loading initial waste processor data, extracted
        from the City of Seattle's website and stored as a list of dictionaries
        in wasteprocessors.salvage_companies. Call from the command line like so:
        >>> import wasteprocessors.models as models
        >>> models.WasteProcessor.load_waste_processor_data(models.all_companies)"""
        for c in all_companies:
            waste_processor, created = cls.objects.get_or_create(company=c['company'])
            waste_processor.description = c['description']
            waste_processor.website = c['website']
            waste_processor.phone = c['phone']
            waste_processor.business_hours = c['business_hours']
            waste_processor.email = c['email']
            waste_processor.address = c['address']
            for m in c['materials_accepted']:
                material, created = MaterialType.objects.get_or_create(material_type=m)
                waste_processor.materials_accepted.add(material)
            waste_processor.save()





