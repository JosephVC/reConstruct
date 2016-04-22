from selenium import webdriver
import unittest

class Setup_Teardown(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(1)

    def tearDown(self):
        self.browser.quit()


class WebPage(Setup_Teardown):

    def test_web_page_title(self):
        self.browser.get ('http://localhost:8000')
        assert 'Salvage App' in self.browser.title


class NewVisitorTest(Setup_Teardown):

    def test_user_can_create_account(self):
        return
    #A new user (Frank - Deconstructors Unlimited) comes to the site
    # Frank creates a new account using the django-registration forms
    # Frank provides a
        # username and
        # a password
        # both are necessary in order to create the account.

class NewVisitorProfilePageTest(Setup_Teardown):

    def test_user_profile_page(self):
        return
    # After creating his account
    # Frank is redirected to a 'profile' page
    # on the profile page Frank is prompted to enter some additional information into an html form.
    # This form includes a field for 'user type'
        # with options of 'contractor' or
        # 'home owner' and
        # a text field for 'company name'.
    # The form also includes
        # a form for the user to add new 'projects'.
            # This 'projects ' form includes
                # a field for 'project type' with
                    # the options of
                        # 'residential construction',
                        # 'commercial construction',
                        # 'new construction',
                        # 'remodel' and
                        # 'homeowner project'.
    # The 'projects' form also includes
        # a field for 'project name'
        # and 'project address'.

class NewVisitorRedirectTest(Setup_Teardown):

    def test_user_redirect_after_forms_complete(self):
        return

    # After entering this information into the forms and saving, the user will be
    # redirected to the main interface for the 'wasteprocessors' app that I'm working on.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
