from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.views import View
from .models import Book
# Create your views here.

class BrowseBook(ListView):
    model = Book
    template_name = 'book/show_book.html'
    context_object_name = 'data'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
    
class SearchView(View):
    template_name = 'book/show_book.html'
    def get(self,request,*args,**kwargs):
        query = request.GET.get('q')
        results = Book.objects.filter(title__icontains=query)
        context = {'results': results, 'query': query}
        return render(request=request, template_name=self.template_name, context=context)