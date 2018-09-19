from concierge_paas_plugin.helper.TokenGenerator import Generator
from django.test import SimpleTestCase

class TokenGeneratorTest(SimpleTestCase):
    def test_expectToken(self):
        token = Generator().create()
        self.assertIsNotNone(token)
    def test_expectTokenIsValid(self):
        token = Generator().create()
        self.assertEqual(token.__len__(), 40)