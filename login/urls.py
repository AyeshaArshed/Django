from django.urls import path, include
from .views import *

urlpatterns = [
    path('',login_view,name='login'),
    path('logout/',logout,name='logout'),
    path('signup/',signup_view,name='signup'),
    path('', include('books.urls')),

]