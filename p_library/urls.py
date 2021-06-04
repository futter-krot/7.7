from django.urls import path
from p_library.views import *
from allauth.account.views import login, logout

urlpatterns = [
	path('', index),
	path('login/', login, name='login'),  
	path('logout/', logout, name='logout'),
]