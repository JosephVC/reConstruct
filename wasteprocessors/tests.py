from django.test import TestCase
from django.test import RequestFactory
from django.core.urlresolvers import resolve
from django.shortcuts import render
from django.contrib.auth.models import User

from wasteprocessors.views import material_search_view
from wasteprocessors.models import UserType, Profile
from wasteprocessors.forms import WasteForm

# Create your tests here.

class MaterialSearchTestCase(TestCase):

    # Used the ebook Real Python Part 3: Advanced Web Development with Django
    # as a reference for writing these tests

    def setUp(self):
        # create models for tests
        self.user = User.objects.create_user('rob', 'rob@email.com', 'password')
        self.user_type = UserType.objects.create(user_type='contractor')
        self.profile = Profile.objects.create(user=self.user, user_type=self.user_type, company='Alford Homes')

        # create a request object using the Django request factory
        request_factory = RequestFactory()
        self.request = request_factory.get('/material-search/')
        self.request.user = self.user

        # instantiate form for template context
        self.form = WasteForm()

    # Routing tests

    def test_url_resolves_to_material_search_view(self):
        material_search = resolve('/material-search/')
        self.assertEqual(material_search.func, material_search_view)

    def test_returns_appropriate_html_response_code(self):
        resp = material_search_view(self.request)
        self.assertEquals(resp.status_code, 200)

    # Template and view tests

    def test_returns_exact_html(self):
        resp = material_search_view(self.request)
        self.assertEquals(
            resp.content,
            render(self.request, "materialsearch.html", context={
                'profile': self.profile,
                'form': self.form
                }
            ).content
        )






