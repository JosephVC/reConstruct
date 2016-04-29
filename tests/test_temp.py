from selenium import webdriverfrom django.test import Client
from myblog.models import Post, Category
import datetime
client = Client()
import unittest


class Setup_Teardown(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.verificationErrors = []

    def tearDown(self):
        self.browser.quit()
        self.assertEqual([], self.verificationErrors)


class HomePage(Setup_Teardown):

    def test_homepage(self):
        response = client.get('/')
        try:
            self.assertEqual(response.status_code, 201)
        except AssertionError as e: 
            self.verificationErrors.append('test_homepage: '+str(e))


class Login(Setup_Teardown):
    def test_login(self):
        response = client.post('/login/', {'username': 'john', 'password': 'smith'})
        try:
            self.assertEqual(response.status_code, 200)
        except AssertionError as e: 
            self.verificationErrors.append('test_login: '+str(e))

# >>> response = c.get('/customer/details/')
# >>> response.content
# '<!DOCTYPE html...'

# class SuperUserTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.su = User.objects.create_superuser('super','','the_correct_password')
#     def test_su_can_login(self):
#         response = self.client.post(reverse('django.contrib.auth.views.login'),
#             {'username': 'super', 'password': 'the_wrong_password'})
#         self.assertEqual(response.status_code,401)

#         # Success redirects to the homepage, so its 302 not 200
#         response = self.client.post(reverse('django.contrib.auth.views.login'),
#             {'username': 'super', 'password': 'the_correct_password'})
#         self.assertEqual(response.status_code,302)



    # def test_web_page_title(self):
    #     from django.core.urlresolvers import reverse
    #     client = Client()

    #     response = client.get(reverse('list_view'))
    #     self.assertEqual(response.status_code, '200')


if __name__ == '__main__':
   unittest.main(warnings='ignore')
