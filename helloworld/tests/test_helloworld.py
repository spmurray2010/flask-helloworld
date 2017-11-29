import os
import helloworld
import unittest
import tempfile

class HelloWorldTestCase(unittest.TestCase):

  def setUp(self):
     self.app = helloworld.app.test_client()
     

  def test_hello(self):
     rv = self.app.get('/')
     assert 'Hello World!' == rv.data
