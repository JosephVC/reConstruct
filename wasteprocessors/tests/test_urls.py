from django.test import TestCase
from django.core.urlresolvers import resolve

from wasteprocessors.views import \
    waste_processor_detail, \
    material_search_view, \
    material_search_results


class WasteprocessorsURLsTestCase(TestCase):

    def test_salvage_companies_url_uses_salvage_companies_list(self):
        """
        Test that the salvage_companies of the site resolves to the 
        salvage_companies_list function
        """
        salvage_companies = resolve('/material-search/waste-processors/1/')
        self.assertEqual(salvage_companies.func, waste_processor_detail)

    def test_material_search_url_uses_material_search_view(self):
        """
        Test that the /profile of the site resolves to the 
        profile_view function
        """
        m_search = resolve('/material-search/project/3/')
        self.assertEqual(m_search.func, material_search_view)


    def test_waste_id_url_uses_material_search_results(self):
        """
        Test that the waste_id (regex) of the site resolves to the 
        material_search_results function
        """
        material_search_res = resolve('/material-search/results/1/')
        self.assertEqual(material_search_res.func, material_search_results)
