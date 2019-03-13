from django.db import models


# Create your models here.
class Fibonacci(models.Model):
    number = models.TextField()
    fib_value = models.TextField()

    def __str__(self):
        return self.number
