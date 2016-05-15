from django.test import TestCase
from django.test import RequestFactory
from django.core.urlresolvers import resolve
from django.shortcuts import render
from django.contrib.auth.models import User

from wasteprocessors.views import material_search_view
from userprofiles.models import UserType, Profile, ProjectType, Project
from wasteprocessors.forms import WasteForm

# create models shared across unit tests.
# or see this for how to use fixtures: http://toastdriven.com/blog/2011/apr/10/guide-to-testing-in-django/
# and this: http://toastdriven.com/blog/2011/apr/17/guide-to-testing-in-django-2/
def user_profile_test_models(self):
    self.user = User.objects.create_user('rob', 'rob@email.com', 'password')
    self.user_type = UserType.objects.create(user_type='contractor')
    self.profile = Profile.objects.create(user=self.user,
                                          user_type=self.user_type,
                                          company='Alford Homes')
    self.project_type = ProjectType.objects.create(project_type='New construction')
    self.project = Project.objects.create(profile=self.profile,
                                          project='Smith Residence',
                                          project_slug='smith-residence',
                                          project_type=self.project_type,
                                          address='123 Smith Street Seattle WA 98115')

# Used the ebook Real Python Part 3: Advanced Web Development with Django
# as a reference for writing these tests

class MaterialSearchTestCase(TestCase):

    # use @classmethod to only run setup once, instead of before each test
    @classmethod
    def setUp(self):
        user_profile_test_models(self)
        # create a request object using the Django request factory
        request_factory = RequestFactory()
        self.request = request_factory.get(
            '/material-search/project/{}/'.format(self.project.project_slug)
            )
        # set request parameters
        self.request.user = self.user
        self.request.project_slug = self.project.project_slug

        # instantiate form for template context
        self.form = WasteForm()

    # Routing tests

    def test_url_resolves_to_material_search_view(self):
        material_search = resolve(
            '/material-search/project/{}/'.format(self.project.project_slug)
            )
        self.assertEqual(material_search.func, material_search_view)

    # add test for POST request, 302 response
    def test_returns_appropriate_html_response_code(self):
        resp = material_search_view(self.request, self.project.project_slug)
        self.assertEquals(resp.status_code, 200)


    # Template and view tests

    def test_returns_exact_html(self):
        resp = material_search_view(self.request, self.project.project_slug)
        self.assertEquals(
            resp.content,
            render(self.request, "materialsearch.html", context={
                'profile': self.profile,
                'project': self.project,
                'form': self.form
                }
            ).content
        )


