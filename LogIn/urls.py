from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('submit', views.submit, name='submit'),
    path('signup', views.signup, name='signup')
]
