from django.urls import path
from . import views

urlpatterns = [
    path('api/signup/', views.API_SignUp.as_view(), name='api_signup'),
    path('api/login/', views.API_Login.as_view(), name='api_login'),
    path('api/profile/', views.API_Profile.as_view(), name='api_profile'),
    path('logout/', views.logoutview, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile')
]
