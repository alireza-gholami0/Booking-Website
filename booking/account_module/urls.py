from django.urls import path
from . import views

urlpatterns = [
    path('api/signup/', views.API_SignUp.as_view()),
    path('api/login/', views.API_Login.as_view()),
    path('signup/', views.signup, name='signup'),
    path('', views.login, name='login')
]
