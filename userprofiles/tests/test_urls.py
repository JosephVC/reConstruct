from django.test import TestCase
from django.core.urlresolvers import resolve

from userprofiles.views import \
    home_view, \
    profile_view, \
    edit_profile_view, \
    create_project_view


class UserprofilesURLsTestCase(TestCase):

    def test_root_url_uses_home_view(self):
        """
        Test that the root of the site resolves to the 
        home_view function
        """
        root = resolve('/')
        self.assertEqual(root.func, home_view)

    def test_profile_url_uses_profile_view(self):
        """
        Test that the /profile of the site resolves to the 
        profile_view function
        """
        profile = resolve('/profile/')
        self.assertEqual(profile.func, profile_view)

    def test_edit_profile_url_uses_edit_profile_view(self):
        """
        Test that the /profile/edit of the site resolves to the 
        edit_profile_view function
        """
        edit_profile = resolve('/profile/edit/')
        self.assertEqual(edit_profile.func, edit_profile_view)

    def test_new_project_url_uses_create_project_view(self):
        """
        Test that the new_project of the site resolves to the 
        create_project_view function
        """
        new_project = resolve('/new-project/')
        self.assertEqual(new_project.func, create_project_view)
