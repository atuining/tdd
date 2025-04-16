from django.test import TestCase


# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")
        self.assertContains(response, "<title>To-Do Lists</title>")
        self.assertContains(response, "<html>")
        self.assertContains(response, "</html>")

    def test_home_page_returns_correct_html_2(self):
        response = self.client.get("/")
        self.assertContains(response, "<title>To-Do Lists</title>")
