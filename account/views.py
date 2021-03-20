from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

from .admin import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic import RedirectView
from django.contrib.auth import logout


class RegisterView(CreateView):
    template_name = 'registration/registration.html'
    form_class = UserCreationForm
    success_url = '../../posts/'

    def form_valid(self, form):
        valid = super().form_valid(form)

        login(self.request, self.object)
        return valid


class LogoutView(RedirectView):

    url = '/account/login/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
