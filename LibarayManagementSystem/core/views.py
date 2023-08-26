
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
# Create your views here.

class Profile(TemplateView):
    template_name = 'core/profile.html'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)