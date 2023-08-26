from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
# Create your views here.

class RegistrationView(CreateView):
    template_name = 'accounts/registration.html'
    form_class = UserRegistrationForm
    context_object_name = 'form'
    success_url = reverse_lazy('login')
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request,*args,**kwargs)

class UserLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'


class UserLogoutView(LogoutView):
    pass