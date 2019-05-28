from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponse
from src.models.account.models import User
from src.models.profile.models import Profile


class RegisterView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home_page')
        return render(request, 'register/index.html', {})


    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        qs = User.objects.filter(email=email)
        if qs.exists():
            return HttpResponseNotFound()
        user = User(email=email)
        user.set_password(password)
        user.save()
        profile = Profile(user=user, username=username, description='BLABLA')
        profile.save()
        return HttpResponse("GOOD")
