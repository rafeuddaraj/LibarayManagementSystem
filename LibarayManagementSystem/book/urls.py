from django.urls import path
from .views import BrowseBook,SearchView

urlpatterns = [
    path('browse-book/',BrowseBook.as_view(),name='show-book'),
    path('search/', SearchView.as_view(), name='search'),
]


