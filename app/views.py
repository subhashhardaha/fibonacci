from django.shortcuts import render
from django.views.generic.base import View

from .models import Fibonacci
from .utils import fibonacci_nth


# Create your views here.

class Home(View):
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        context={}
        print("get")
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        print("post")
        n=request.POST['fibonacci_number']
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
        return render(request, self.template_name, context)
