from concierge_paas_plugin.helper.TokenGenerator import Generator
from django.test import SimpleTestCase

class TokenGeneratorTest(SimpleTestCase):
    def test_expectToken(self):
        token = Generator().create()
        self.assertIsNotNone(token)
    def test_expectTokenIsValid(self):
        token = Generator().create("ooteyiwoatewa")
        print(str(token))
        self.assertEqual(str(token).__len__(), 4)