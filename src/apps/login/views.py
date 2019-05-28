from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login


class LoginView(View):

    def post(self, request, *args, **kwargs):
        email       = request.POST.get('email')
        password    = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home_page')
        else:
            return redirect('home:home_page')
