import time

from django.shortcuts import render
from django.views.generic.base import View

from .models import Fibonacci
from .utils import fibonacci_nth, MatrixFibonacci
from datetime import timedelta

# Create your views here.

class Home(View):
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        context={}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        start = time.time()

        context = {}
        n=request.POST['fibonacci_number']

        if n:
            context['fibonacci_number']=n

            if Fibonacci.objects.filter(number=n).exists():
                obj = Fibonacci.objects.get(number=n)
                value = obj.fib_value
                context['fibonacci_value'] = value
                #time_taken_direct='0'
                time_taken_mat='0'
            else:
                # start_d = time.time()
                # fibonacci_nth(int(n))
                # time_taken_direct=str(timedelta(seconds=time.time()-start_d))
                start_m = time.time()
                mf=MatrixFibonacci()
                ans=mf.get_number(int(n))
                time_taken_mat = str(timedelta(seconds=time.time() - start_m))
                context['fibonacci_value'] = ans
                data = Fibonacci(number=n, fib_value=ans)
                data.save()
        end = time.time()
        time_taken=str(timedelta(seconds=end-start))
        context['total_time_taken']=time_taken
        #context['time_taken_direct'] = time_taken_direct
        context['time_taken_mat'] = time_taken_mat

        return render(request, self.template_name, context)
