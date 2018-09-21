from django.test import TestCase
from django.urls import reverse_lazy
from concierge_paas_plugin.models import Configuration, User
from concierge_paas_plugin.views import create_profile, queryprofile
from rest_framework.test import force_authenticate, APIRequestFactory

class CreateProfileTest(TestCase):
    def setUp(self):
        self.configuration = Configuration(token='045d5617bbbd13c523be1fa6b86486e3c8a57b00', end_point="http://localhost:8001/protected", default=True, trigger=True)
        self.configuration.save()

        self.user = User(username='user',name='somename',email='username@name.test')
        self.user.save()
    def test_createBasicProfile(self):
        userid = 123
        user = User.objects.get(username=self.user.username)

        create_request = self.createRequest(user, 'create_profile')
        create_profile(create_request, userid, "username", "user@user.com")

        queryProfile_request = self.createRequest(user, 'queryprofile')
        response = queryprofile(queryProfile_request, 123)
        print(response)
        # self.assertEqual(response, "12564")

    def createRequest(self, user, viewName):
        factory = APIRequestFactory()
        request = factory.get(reverse_lazy(viewName))
        request.user = user
        force_authenticate(request, user=user)
        return request