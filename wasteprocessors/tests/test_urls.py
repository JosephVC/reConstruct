from django.test import TestCase
from django.core.urlresolvers import resolve

from wasteprocessors.views import \
    salvage_companies_list, \
    material_search_view, \
    material_search_results


class WasteprocessorsURLsTestCase(TestCase):

    def test_salvage_companies_url_uses_salvage_companies_list(self):
        """
        Test that the salvage_companies of the site resolves to the 
        salvage_companies_list function
        """
        salvage_companies = resolve('/salvage-companies/')
        self.assertEqual(salvage_companies.func, salvage_companies_list)

    def test_material_search_url_uses_material_search_view(self):
        """
        Test that the /profile of the site resolves to the 
        profile_view function
        """
        m_search = resolve('/project/P<project_slug>-a/')
        self.assertEqual(m_search.func, material_search_view)


    def test_waste_id_url_uses_material_search_results_A(self):
        """
        Test that the waste_id (regex) of the site resolves to the 
        material_search_results function
        """
        material_search_res = resolve('material-search/results/1/')
        self.assertEqual(material_search_res.func, material_search_results)

    def test_waste_id_url_uses_material_search_results_B(self):
        """
        Test that the waste_id (regex) of the site resolves to the 
        material_search_results function
        """
        material_search_res = resolve('material-search/results/P<waste_id>2/')
        self.assertEqual(material_search_res.func, material_search_results)