from mixer.backend.django import mixer
import pytest

@pytest.mark.django_db
class TestModels:

    def test_if_post_is_added(self):
        post = mixer.blend('blog.Post', title='post 1')
        assert post.title == 'post 1'
