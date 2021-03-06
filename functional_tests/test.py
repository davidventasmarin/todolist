import unittest
import time

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

MAX_WAIT = 10
class NewVisitorTest(LiveServerTestCase):
   
    def setUp(self):
        self.navegador = webdriver.Firefox()        

    def tearDown(self):
        self.navegador.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.navegador.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)        

    def test_can_start_a_list_and_retieve_it_later(self):

        #Edit has heard about a cool new online to-do app. She goes 
        #to check out its homepage
        self.navegador.get(self.live_server_url)

        #She notices the page title and header mention to-do list
        self.assertIn('To-Do', self.navegador.title)
        header_test = self.navegador.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_test)

        #She is invited to enter a to-do item straight away
        inputbox = self.navegador.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 
                        'Enter a to-do item')
        #She types "Buy peacock feathers" into a text box (Edith's hobby
        #is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        #When she hits enter, the page updates, and how the page lists
        #"1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        #There is still a text box inviting her to add another item. She
        #enters "User peacock feathers to make a fly" (Edith is very methodical)
        inputbox = self.navegador.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        #The page updates again, and now shows both items on her list
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

        #Edith wonders whether the site will remember her list. Then she sees
        #that the site has generated a unique URL for her -- there is some
        #explanatory text to that effect.
        #self.fail("finish the test!")

        #She visits that URL - her to-do list is still there.

        #Satisfied, she goes back to sleep

    def test_can_start_a_list_for_one_user(self):

        #Edit has heard about a cool new online to-do app. She goes 
        #to check out its homepage
        self.navegador.get(self.live_server_url)

        #She notices the page title and header mention to-do list
        self.assertIn('To-Do', self.navegador.title)
        header_test = self.navegador.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_test)

        #She is invited to enter a to-do item straight away
        inputbox = self.navegador.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 
                        'Enter a to-do item')
        #She types "Buy peacock feathers" into a text box (Edith's hobby
        #is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        #When she hits enter, the page updates, and how the page lists
        #"1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        #There is still a text box inviting her to add another item. She
        #enters "User peacock feathers to make a fly" (Edith is very methodical)
        inputbox = self.navegador.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        #The page updates again, and now shows both items on her list
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        #Edith wonders whether the site will remember her list. Then she sees
        #that the site has generated a unique URL for her -- there is some
        #explanatory text to that effect.
        #self.fail("finish the test!")

        #She visits that URL - her to-do list is still there.

        #Satisfied, she goes back to sleep

    

    def test_multiple_users_can_start_lists_at_different_url(self):
        # Edit starts a new to-do list
        self.navegador.get(self.live_server_url)
        inputbox = self.navegador.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # she notices that her list has a unique URL
        edit_list_url = self.navegador.current_url
        self.assertRegex(edit_list_url, '/lists/.+')

        # Now a new user, Francis, comes along to the site

        # We use a new browser session to make sure that no information
        # of Edith's is  coming through from cookies etc.
        self.navegador.quit()
        self.navegador = webdriver.Firefox()

        # Francis visits the home page. There is no sign of Edith's
        # list
        self.navegador.get(self.live_server_url)
        page_text = self.navegador.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis starts a new list by entering a new item. He 
        # is less interesting than Edith...
        inputbox = self.navegador.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Francis get his own unique URL
        francis_list_url = self.navegador.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edit_list_url)

        # Again, there is no trace of Edith's list
        page_text = self.navegador.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

    def test_layout_and_styling(self):
        # edit goes to the home page
        self.navegador.get(self.live_server_url)
        self.navegador.set_window_size(1024, 789)

        # she notices the input box is nicely centered
        inputbox = self.navegador.find_element_by_id('id_new_item')
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        inputbox = self.navegador.find_element(By.ID, 'id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

    

