from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from lists.views import index_page


class IndexPageTest(TestCase):
    """Тест главной страницы"""

    def test_root_url_resolves_to_index_page_view(self):
        """Тест: корневой url обрабатывается правильной вьюхой"""
        view = resolve("/")
        self.assertEqual(view.func, index_page)

    def test_home_page_returns_correct_html(self):
        """Тест: домашняя страница возвращает правильный html"""
        request = HttpRequest()
        response = index_page(request)
        html = response.content.decode("utf8")

        self.assertTrue(html.startswith("<html>"))
        self.assertIn("<title>To-Do lists</title>", html)
        self.assertTrue(html.endswith("</html>"))
