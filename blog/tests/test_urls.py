from django.urls import reverse, resolve

class TestUrls:

    def test_home_url(self):
        path = reverse('blog:home')
        
        # This resolve it resolves the path view name and return it.
        assert resolve(path).view_name == 'blog:home'
