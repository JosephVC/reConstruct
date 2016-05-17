from django.test import TestCase
from django.test import RequestFactory
from django.core.urlresolvers import resolve
from django.shortcuts import render, get_list_or_404
from django.contrib.auth.models import User

from wasteprocessors.views import material_search_view
from userprofiles.models import Profile, Project
from wasteprocessors.models import WasteType, MaterialType, Waste
from wasteprocessors.forms import WasteForm

# write test case for each url pattern that tests routes, views, model methods
# forms, custom template tags etc. associated with this pattern
class MaterialSearchTestCase(TestCase):
    fixtures = ['userprofile_test_data.json', 'wasteprocessors_test_data.json']

    # use @classmethod to only run setup once, instead of before each test
    @classmethod
    def setUp(self):
        # instantiate models for tests
        self.user = User.objects.get(pk=1)
        self.profile = Profile.objects.get(pk=1)
        self.project = Project.objects.get(pk=1)
        self.waste_type = WasteType.objects.get(pk=1)
        self.material_type = MaterialType.objects.get(pk=1)
        # create a request object using the Django request factory
        request_factory = RequestFactory()
        self.request = request_factory.get(
            '/material-search/project/{}/'.format(self.project.id)
            )
        self.post = request_factory.post(
            '/material-search/project/{}/'.format(self.project.id),
            {'waste_type': self.waste_type.id,
            'material_type': self.material_type.id}
        )
        # set request parameters
        self.request.user = self.user
        self.post.user = self.user
        self.request.project_id = self.project.id
        # instantiate form for template context
        self.form = WasteForm()

    # Routing tests

    def test_url_resolves_to_material_search_view(self):
        material_search = resolve(
            '/material-search/project/{}/'.format(self.project.id)
            )
        self.assertEqual(material_search.func, material_search_view)

    def test_returns_appropriate_html_response_code(self):
        resp = material_search_view(self.request, self.project.id)
        self.assertEquals(resp.status_code, 200)

    def test_redirect_on_post_request(self):
        resp = material_search_view(self.post, self.project.id)
        self.assertEquals(resp.status_code, 302)

    # Template and view tests

    def test_returns_exact_html(self):
        resp = material_search_view(self.request, self.project.id)
        self.assertEquals(
            resp.content,
            render(self.request, "materialsearch.html", context={
                'profile': self.profile,
                'project': self.project,
                'form': self.form
                }
            ).content
        )

    def test_response_content(self):
        resp = material_search_view(self.request, self.project.id)
        self.assertContains(resp, self.profile.company)
        self.assertContains(resp, self.project.project)

    def test_forms_include_all_waste_and_material_types(self):
        resp = material_search_view(self.request, self.project.id)
        waste_types = get_list_or_404(WasteType)
        material_types = get_list_or_404(MaterialType)
        for waste_type in waste_types:
            self.assertContains(resp, waste_type)
        for material_type in material_types:
            self.assertContains(resp, material_type)



