from django.test import TestCase
from django.urls import resolve
from lists.views import index_page


class IndexPageTest(TestCase):
    """Тест главной страницы"""

    def test_root_url_resolves_to_index_page_view(self):
        """Тест: корневой url обрабатывается правильной вьюхой"""
        view = resolve("/")
        self.assertEqual(view.func, index_page)
