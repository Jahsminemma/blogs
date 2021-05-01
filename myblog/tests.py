from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.core import mail
from .models import Post
from .forms import CommentForm


class BlogTests(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.post = Post.objects.create(
            title='A good title',
            body='Nice body',
            author=self.user,
        )

    def test_string_representation(self):

        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):

        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_secure_page(self):
        User = get_user_model()
        self.client.login(username='testuser', password='secret')
        response = self.client.get('/admin/login')
        self.assertEquals(response.status_code, 302)

    def test_logout(self):
        self.client.login(username='testuser', password="secret")
        response = self.client.get('/admin/login')
        self.assertEquals(response.status_code, 302)
        self.client.logout()
        response = self.client.get('/admin')
        self.assertEquals(response.status_code, 301)

    def test_comment(self):
        form_data = {'comment': 'comment', 'name': 'name'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_actual_reset_password(self):
        pass
