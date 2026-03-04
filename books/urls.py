from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',BookListView.as_view(),name='list_book'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='detail_book'),
    path('book/create', BookCreateView.as_view(), name='create_book'),
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='update_book'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='delete_book'),
]
