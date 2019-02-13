from django.test import SimpleTestCase
from django.urls import resolve, reverse
from blog.views import PostListView, PostDetailView, PostCreateView, PostDeleteView
class TestUrls(SimpleTestCase):

    def test_home_url(self):
        url = reverse('blog:home')
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_create_url(self):
        url = reverse('blog:new')
        self.assertEquals(resolve(url).func.view_class, PostCreateView)
    
    def test_detail_url(self):
        url = reverse('blog:detail', kwargs={'pk': '1'})
        self.assertEquals(resolve(url).func.view_class, PostDetailView)

    def test_delete_url(self):
        url = reverse('blog:delete', kwargs={'pk': '1'})
        self.assertEquals(resolve(url).func.view_class, PostDeleteView)
        