from django.test import TestCase
from django.core.urlresolvers import resolve

from wasteprocessors.views import salvage_companies_list
from wasteprocessors.views import material_search_view
from wasteprocessors.views import material_search_results


class WasteprocessorsURLsTestCase(TestCase):

    def test_salvage_companies_url_uses_salvage_companies_list(self):
        """
        Test that the salvage_companies of the site resolves to the 
        salvage_companies_list function
        """
        print ("made it to here\n")
        salvage_companies = resolve('/salvage-companies/')
        print ("salvage_companies = ", salvage_companies)
        print ("salvage_companies_list = ", salvage_companies_list)
        self.assertEqual(salvag_companies.func, salvage_companies_list)

    def test_material_search_url_uses_material_search_view(self):
        """
        Test that the /profile of the site resolves to the 
        profile_view function
        """
        m_search = resolve('/project/P<project_slug>-a/')
        self.assertEqual(m_search.func, material_search_view)


    def test_waste_id_url_uses_material_search_results(self):
        """
        Test that the waste_id (regex) of the site resolves to the 
        material_search_results function
        """
        material_search_res = resolve('/results/P<waste_id>2/')
        self.assertEqual(material_search_res.func, material_search_results)

    # def test_edit_profile_url_uses_edit_profile_view(self):
    #     """
    #     Test that the /profile/edit of the site resolves to the 
    #     edit_profile_view function
    #     """
    #     edit_profile = resolve('/profile/edit/')
    #     self.assertEqual(edit_profile.func, edit_profile_view)

    # def test_new_project_url_uses_create_project_view(self):
    #     """
    #     Test that the new_project of the site resolves to the 
    #     create_project_view function
    #     """
    #     new_project = resolve('/new-project/')
    #     self.assertEqual(new_project.func, create_project_view)

##### done to here
    # def test_solo_details_url(self):
    #     """
    #     Test that the URL for SoloDetail resolves to the correct view function
    #     """
    #     solo_detail = resolve( '/recordings/kind-of-blue/all-blues/cannonball-adderley/')

    #     self.assertEqual(solo_detail.func.__name__, 'solo_detail')
    #     self.assertEqual(solo_detail.kwargs['album'], 'kind-of-blue')
    #     self.assertEqual(solo_detail.kwargs['track'], 'all-blues')
    #     self.assertEqual(solo_detail.kwargs['artist'], 'cannonball-adderley')
