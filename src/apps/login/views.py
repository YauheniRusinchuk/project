from django.views import View
from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login


class LoginView(View):

    def post(self, request, *args, **kwargs):
        email       = request.POST.get('email')
        password    = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return redirect('home_home_page')
