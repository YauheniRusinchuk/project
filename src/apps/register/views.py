from django.views import View
from django.shortcuts import render, redirect


class RegisterView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home_page')
        return render(request, 'register/index.html', {})
