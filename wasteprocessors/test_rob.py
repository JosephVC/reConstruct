from django.test import TestCase
from django.test import RequestFactory
from django.core.urlresolvers import resolve
from django.shortcuts import render, get_list_or_404
from django.contrib.auth.models import User
from django.utils.html import escape

from wasteprocessors.views import material_search_view, material_search_results
from userprofiles.models import Profile, Project
from wasteprocessors.models import WasteType, MaterialType, Waste, WasteProcessor
from wasteprocessors.forms import WasteForm, SearchFilterForm

# write test case for each url pattern that tests routes, views, model methods
# forms, custom template tags etc. associated with this pattern
class MaterialSearchTestCase(TestCase):
    fixtures = ['userprofile_test_data.json', 'wasteprocessors_test_data.json']

    # use @classmethod to only run setup once, instead of before each test
    @classmethod
    def setUpTestData(cls):
        # instantiate models for tests
        cls.user = User.objects.get(pk=1)
        cls.profile = Profile.objects.get(pk=1)
        cls.project = Project.objects.get(pk=1)
        cls.waste_type = WasteType.objects.get(pk=1)
        cls.material_type = MaterialType.objects.get(pk=1)
        # create a request object using the Django request factory
        request_factory = RequestFactory()
        cls.request = request_factory.get(
            '/material-search/project/{}/'.format(cls.project.id)
            )
        cls.post = request_factory.post(
            '/material-search/project/{}/'.format(cls.project.id),
            {'waste_type': cls.waste_type.id,
            'material_type': cls.material_type.id}
        )
        # set request parameters
        cls.request.user = cls.user
        cls.post.user = cls.user
        # instantiate form for template context
        cls.form = WasteForm()

    # Routing tests

    def test_url_resolves_to__view(self):
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

class MaterialSearchResultsTestCase(TestCase):
    fixtures = ['userprofile_test_data.json', 'wasteprocessors_test_data.json']

    @classmethod
    def setUpTestData(cls):
        # instantiate models for tests
        cls.user = User.objects.get(pk=1)
        cls.project = Project.objects.get(pk=1)
        cls.waste_type = WasteType.objects.get(pk=1)
        cls.material_type = MaterialType.objects.get(pk=1)
        cls.waste = Waste.objects.create(project=cls.project,
                                          waste_type=cls.waste_type,
                                          material_type=cls.material_type)
        cls.material_processors = WasteProcessor.objects.filter(
            materials_accepted=cls.waste.material_type)
        cls.material_processors = cls.material_processors.filter(
            waste_types_accepted=cls.waste.waste_type)
        # create a request object using the Django request factory
        cls.request_factory = RequestFactory()
        cls.request = cls.request_factory.get(
            '/material-search/results/{}/'.format(cls.waste.id)
            )
        # set request parameters
        cls.request.user = cls.user
        # instantiate form for template context
        cls.form = SearchFilterForm()

    # Routing tests

    def test_url_resolves_to__view(self):
        url = resolve(
            '/material-search/results/{}/'.format(self.waste.id)
            )
        self.assertEqual(url.func, material_search_results)

    def test_returns_appropriate_html_response_code(self):
        resp = material_search_results(self.request, self.waste.id)
        self.assertEquals(resp.status_code, 200)

    # Template and view tests

    def test_returns_exact_html(self):
        resp = material_search_results(self.request, self.waste.id)
        self.assertEquals(
            resp.content,
            render(self.request, "materialsearchresults.html", context={
                'profile': self.waste.project.profile,
                'project': self.waste.project,
                'material_type': self.waste.material_type,
                'waste_type': self.waste.waste_type,
                'material_processors': self.material_processors,
                'form': self.form,
                }
            ).content
        )

    def test_response_content(self):
        resp = material_search_results(self.request, self.waste.id)
        self.assertContains(resp, 'Search results')
        for material_processor in self.material_processors:
            self.assertContains(resp, escape(material_processor))

    def test_will_purchase_post_filter(self):
        will_purchase_post = self.request_factory.post(
            '/material-search/results/{}/'.format(self.waste.id),
            {'will_purchase': 'on'}
            )
        resp = material_search_results(will_purchase_post, self.waste.id)
        filtered_results = self.material_processors.filter(will_purchase=True)
        for material_processor in filtered_results:
            self.assertContains(resp, escape(material_processor))

    def test_accepts_dontations_post_filter(self):
        accepts_donations_post = self.request_factory.post(
            '/material-search/results/{}/'.format(self.waste.id),
            {'accepts_donations': 'on'}
            )
        resp = material_search_results(accepts_donations_post, self.waste.id)
        filtered_results = self.material_processors.filter(accepts_donations=True)
        for material_processor in filtered_results:
            self.assertContains(resp, escape(material_processor))

    def test_will_pick_up_post_filter(self):
        will_pick_up_post = self.request_factory.post(
            '/material-search/results/{}/'.format(self.waste.id),
            {'will_pick_up': 'on'}
            )
        resp = material_search_results(will_pick_up_post, self.waste.id)
        filtered_results = self.material_processors.filter(will_pick_up=True)
        for material_processor in filtered_results:
            self.assertContains(resp, escape(material_processor))

    def test_all_search_filters_combined(self):
        combined_filters_post = self.request_factory.post(
            '/material-search/results/{}/'.format(self.waste.id),
            {'will_purchase': 'on',
             'accepts_donations': 'on',
             'will_pick_up': 'on'}
            )
        resp = material_search_results(combined_filters_post, self.waste.id)
        filtered_results = self.material_processors.filter(will_purchase=True)
        filtered_results = filtered_results.filter(accepts_donations=True)
        filtered_results = filtered_results.filter(will_pick_up=True)
        for material_processor in filtered_results:
            print(resp.content)
            self.assertContains(resp, escape(material_processor))

