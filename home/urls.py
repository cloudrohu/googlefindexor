from django.urls import path

from home.views import IndexView
from .import views 

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'), 

    
]