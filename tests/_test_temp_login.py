from selenium import webdriver
from django.test import Client
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



class Visitor_Test(Setup_Teardown):
    def test_for_visitor(self):
        response = client.post('/login/?visitor=false', {'name': 'fred', 'passwd': 'secret'})
        try:
            self.assertEqual(response.status_code, 200)
        except AssertionError as e: 
            self.verificationErrors.append('test_for_visitor: '+str(e))



if __name__ == '__main__':
   unittest.main(warnings='ignore')
