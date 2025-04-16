import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_todo_list(self) -> None:
        # Nami has heard about a new todo list app
        # She goes to check out its homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention todo lists
        self.assertIn("To-do", self.browser.title)

        # She is invited to enter a to-do item straight away
        self.fail("Finish the test!")

        # She types "Send wave" into a text box

        # When she hits enter, the page updates, and now the page lists
        # "1. Send wave" as an item in the to-do list

        # There is a still a text box inviting her to add another item
        # She enters "Autoattack enemy"

        # The page updates again and now shoes both items on her list

        # Satisfied, she goes back to the fountain


if __name__ == "__main__":
    unittest.main()
