from django.test import TestCase

from .utils import MatrixFibonacci
from .models import Fibonacci


# Create your tests here.
class FibonacciTestCase(TestCase):
    def test_home(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    # test case postive
    def test_home_postive(self):
        resp = self.client.post('/', {'fibonacci_number': '675'})
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('fibonacci_value' in resp.context)
        self.assertEqual(resp.context['fibonacci_value'], '521401368331405065117389673092721167865606665536905240054000465695003287479466298469643896877133715080215034906732232054782240651067620552450')

    # test case for negative number
    def test_home_negative(self):
        resp = self.client.post('/', {'fibonacci_number': '-3'})
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('message1' in resp.context)
        self.assertEqual(resp.context['message1'], 'Enter postive number only')

    # models test cases
    def create_fibonacci(self, number="45", fib_value="1134903170"):
        return Fibonacci.objects.create(number=number, fib_value=fib_value)

    def test_fibonacci_creation(self):
        f = self.create_fibonacci()
        self.assertTrue(isinstance(f, Fibonacci))
        self.assertEqual(f.__str__(), f.number)

    # util function test case matrix multiplication
    def test_util_function(self):
        mf = MatrixFibonacci()
        n=32
        ans = mf.get_number(int(n))
        self.assertEqual(ans, 2178309)
