import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.navegador = webdriver.Firefox()        

    def tearDown(self):
        self.navegador.quit()

    def test_can_start_a_list_and_retieve_it_later(self):

        #Edit has heard about a cool new online to-do app. She goes 
        #to check out its homepage
        self.navegador.get('http://localhost:8000')

        #She notices the page title and header mention to-do list
        self.assertIn('To-Do', self.navegador.title)
        self.fail("finish the test!")


        #She is invited to enter a to-do item straight away

        #She types "Buy peacock feathers" into a text box (Edith's hobby
        #is tying fly-fishing lures)

        #When she hits enter, the page updates, and how the page lists
        #"1: Buy peacock feathers" as an item in a to-do list

        #There is still a text box inviting her to add another item. She
        #enters "User peacock feathers to make a fly" (Edith is very methodical)

        #The page updates again, and now shows both items on her list

        #Edith wonders whether the site will remember her list. Then she sees
        #that the site has generated a unique URL for her -- there is some
        #explanatory text to that effect.

        #She visits that URL - her to-do list is still there.

        #Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main()
