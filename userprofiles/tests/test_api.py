from django.core.urlresolvers import resolve

from rest_framework.test import APITestCase

from albums.models import \
    UserType, Profile, ProjectType, Project


class UserProfileAPITestCase(APITestCase):

    def setUp(self):
        self.giant_steps = UserType.objects.create(name='Giant Steps', slug='giant-steps')
        self.mr_pc = Profile.objects.create(name='Mr. PC', slug='mr-pc', album=self.giant_steps)
        self.giant_steps = ProjectType.objects.create(name='Giant Steps', slug='giant-steps')
        self.mr_pc = Project.objects.create(name='Mr. PC', slug='mr-pc', album=self.giant_steps)

    def test_UserType(self):
        """
        Test that we can can create a UserType
        """
        post_data = {'user_type': 'Builder'}
        response = self.client.post('/api/solos/', data=post_data, format='json')

        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(response.data, {
            'url': 'http://testserver/api/solos/1/',
            'artist': 'John Coltrane',
            'slug': 'john-coltrane',
            'instrument': 'saxophone',
            'start_time': '0:24',
            'end_time': '3:21',
            'track': 'http://testserver/api/tracks/1/'
        })

    def test_solo_list_route(self):
        """ Test that we've got routing set up for Solos
        """
        route = resolve('/api/solos/')

        self.assertEqual(route.func.__name__, 'SoloViewSet')