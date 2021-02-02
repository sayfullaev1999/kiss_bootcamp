from django.test import TestCase
from django.urls import reverse
from django.utils.text import slugify

from ..models import Project
from account.models import User


class ProjectModelTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username='some_user',
            first_name='First name',
            last_name='Last name',
            email='user1@example.com',
        )
        self.user.set_password('PassUser123')
        self.user.save()
        self.project = Project.objects.create(
            name='some project',
            info='some text',
            image='some_image.jpg',
            site='https://some.site.example',
        )
        self.project.users.add(self.user)

    def test_project_get_absolute_url(self):
        url = reverse('project_detail_url', kwargs={'slug': slugify('some project')})
        self.assertEquals(self.project.get_absolute_url(), url)

    def test_object_name_is_project_name(self):
        self.assertEquals(str(self.project), 'some project')
