from django.test import TestCase
from .models import Degree, requiredCourses

# Create your tests here.
class TestSimpleComponent(TestCase):
    def test_basic_sum(self):
        assert 1+1 == 2
        #assert 1+1 == 3

#test models 
class TestDegreeModel(TestCase): 
    """Test the degree model"""
    def setUp(self):
        self.p = Degree(major_code='703', degree_name='CIS', college_name='Business')
    def test_create_degree(self):
        self.assertIsNotNone(self.p, Degree)
    def test_str_representation(self):
        self.assertEquals(str(self.p), "703")




