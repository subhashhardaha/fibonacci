from django.shortcuts import render

from .models import Fibonacci
from .utils import fibonacci_nth

# Create your views here.
def home(request):
    context = {}
    n = request.GET.get('fibonacci_number', None)
    if n:
        if Fibonacci.objects.filter(number=n).exists():
            obj = Fibonacci.objects.get(number=n)
            value = obj.fib_value
            context['fibonacci_value'] = value
        else:
            ans = fibonacci_nth(int(n))
            context['fibonacci_value'] = ans
            data = Fibonacci(number=n, fib_value=ans)
            data.save()
    return render(request, 'app/index.html', context)