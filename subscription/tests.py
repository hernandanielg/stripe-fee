from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from .models import User

# Create your tests here.
class UserTestCase(TestCase):

    user = User()

    def setUp(self):
        self.user = User.objects.create(name="joe",email="joe@mail.com")

    def test_user_is_registered(self):
        self.assertIs(User.is_registered(self.user.email),True)

class FunctionalTestCase(LiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def tearDown(self):
        pass
        #self.driver.quit()

    def test_user_can_subscribe(self):
        driver = self.driver

        name = "Some Name"
        email = "some@e.mail"

        card = {
            'card_number': '4242424242424242',
            'exp_month': '01',
            'exp_year': '2017',
            'cvc': '123'
        }

        driver.get("http://localhost:8000")
        driver.find_element_by_id("btn-signup").click()
        driver.find_element_by_name("name").send_keys(name)
        driver.find_element_by_name("email").send_keys(email)
        driver.find_element_by_name("card_number").send_keys(card['card_number'])
        driver.find_element_by_name("exp_month").send_keys(card['exp_month'])
        driver.find_element_by_name("exp_year").send_keys(card['exp_year'])
        driver.find_element_by_name("cvc").send_keys(card['cvc'])
        driver.find_element_by_id("btn-subscribe").click()
        alert = driver.find_element_by_id("message-alert")

        self.assertTrue("subscribed" in alert.text)

    def test_invalid_card_exception(self):
        driver = self.driver

        name = "Another Name"
        email = "another@e.mail"

        card = {
            'card_number': '0000000000000000',
            'exp_month': '01',
            'exp_year': '2017',
            'cvc': '123'
        }

        driver.get("http://localhost:8000")
        driver.find_element_by_id("btn-signup").click()
        driver.find_element_by_name("name").send_keys(name)
        driver.find_element_by_name("email").send_keys(email)
        driver.find_element_by_name("card_number").send_keys(card['card_number'])
        driver.find_element_by_name("exp_month").send_keys(card['exp_month'])
        driver.find_element_by_name("exp_year").send_keys(card['exp_year'])
        driver.find_element_by_name("cvc").send_keys(card['cvc'])
        driver.find_element_by_id("btn-subscribe").click()
        alert = driver.find_element_by_id("message-alert")

        self.assertTrue("card number is incorrect" in alert.text)
