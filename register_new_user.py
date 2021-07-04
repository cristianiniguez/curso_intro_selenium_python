import unittest
from selenium import webdriver


class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./drivers/chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo.onestepcheckout.com')

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a').click()
        driver.find_element_by_link_text('Log In').click()

        create_account_button = driver.find_element_by_xpath(
            '//*[@id="login-form"]/div/div[1]/div[2]/a')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element_by_id('firstname')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button')

        self.assertTrue(
            first_name.is_enabled() and last_name.is_enabled() and email_address.is_enabled()
            and password.is_enabled() and confirm_password.is_enabled()
            and news_letter_subscription.is_enabled() and submit_button.is_enabled())

        first_name.send_keys('Test')
        last_name.send_keys('Test')
        email_address.send_keys('test@test.com')
        password.send_keys('test')
        confirm_password.send_keys('test')
        submit_button.click()

    def tearDown(self):
        return super().tearDown()


if __name__ == '__main__':
    unittest.main(verbosity=2)
