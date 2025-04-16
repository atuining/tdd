from django.http import HttpRequest
from django.test import TestCase
from lists.views import home_page


# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html: str = response.content.decode("utf-8")
        self.assertIn("<title>To-Do Lists</title>", html)
        self.assertTrue(html.startswith("<html>"))
        self.assertTrue(html.endswith("</html>"))
