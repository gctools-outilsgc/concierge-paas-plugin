from django.test import TestCase
from concierge_paas_plugin.helper.TokenGenerator import Generator
from concierge_paas_plugin.models import Configuration
from concierge_paas_plugin.views import Profile

class CreateProfileTest(TestCase):
    def setUp(self):
        new_token = Generator().create()
        self.configuration = Configuration(token=new_token, end_point="http://localhost:8001/protected", default=True)
        self.configuration.save()
    def test_createBasicProfile(self):
        userid = "123"
        Profile.create(userid, "username", "user@user.com")
        response = Profile().queryprofile(123)
        print(response)
        # self.assertEqual(response, "12564")