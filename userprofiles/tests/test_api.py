from django.core.urlresolvers import resolve

# Added djangorestframework===3.3.3 to requirements.txt to 
# cover this import
from rest_framework.test import APITestCase

# used to support backend logon
from django.contrib.auth import authenticate, get_backends

from userprofiles.models import \
    UserType, Profile, ProjectType, Project


class UserProfileAPITestCase(APITestCase):

    def setUp(self):
        # self.giant_steps = UserType.objects.create(name='Giant Steps', slug='giant-steps')
        # self.mr_pc = Profile.objects.create(name='Mr. PC', slug='mr-pc', album=self.giant_steps)
    #     self.giant_steps = ProjectType.objects.create(name='Giant Steps', slug='giant-steps')
    #     self.mr_pc = Project.objects.create(name='Mr. PC', slug='mr-pc', album=self.giant_steps)
        pass

    def test_UserType(self):
        """
        Test that we can can create a UserType
        """
        # testing imports
        a = get_backends()
        get_backends()
        print('\nget_backends = ', a)
        b = authenticate(username=1, password='master')
        authenticate(username=1, password='master')
        print('\nauthentication = ', b)
        post_data = {'user_type': 'Contractor',\
                    'company': 'Little Red School',\
                    'phone': '206-232-0995',\
                    'address': '323 NE 57th Street',\
                    }
        response = self.client.post('/profile/edit', \
                        data=post_data, format='json')
#        self.assertTrue(response.request.user.is_authenticated())
        self.assertTrue(response.request.user_id.is_authenticated())

        self.assertEqual(response.status_code, 201, response.data)
        # self.assertEqual(response.data, {
        #     'url': 'http://testserver/api/solos/1/',
        #     'artist': 'John Coltrane',
        #     'slug': 'john-coltrane',
        #     'instrument': 'saxophone',
        #     'start_time': '0:24',
        #     'end_time': '3:21',
        #     'track': 'http://testserver/api/tracks/1/'
        # })

    def test_solo_list_route(self):
        """ Test that we've got routing set up for Solos
        """
        route = resolve('/api/solos/')

        self.assertEqual(route.func.__name__, 'SoloViewSet')