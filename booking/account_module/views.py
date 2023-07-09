from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from ratelimit.decorators import ratelimit
from ratelimit.exceptions import Ratelimited
# from ratelimit.decorators import ratelimit
# from ratelimit.exceptions import Ratelimited
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from .models import User
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as auth_login
from rest_framework.views import status
from django.contrib.auth import login as auth_login
from django.utils import timezone
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# from django_ratelimit.decorators import ratelimit
# from django_ratelimit.exceptions import Ratelimited

class API_Profile(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')
        print(email)
        print(phone_number)
        if email and email != self.request.user.email and User.objects.filter(email=email).exists():
            return Response({'error': 'This email address is already in use.'}, status=status.HTTP_400_BAD_REQUEST)
        if phone_number and phone_number != self.request.user.phone_number and User.objects.filter(
                phone_number=phone_number).exists():
            return Response({'error': 'This phone number is already in use.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(self.request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class API_SignUp(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)



class API_Login(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        ratelimit(keys='ip', rate='5/m', method='POST', block=True)
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(email__iexact=email).first()
        if user:
            pas = user.check_password(password)
            if pas:
                auth_login(request, user)
                user.last_login = timezone.now()
                user.save()
                request.session['user_id'] = user.id
                response = Response({'msg': 'successful'}, status=status.HTTP_200_OK)
                response.set_cookie('key', 'value', max_age=3600, secure=True, httponly=True)
                return response

            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    def handle_exception(self, exc):
        if isinstance(exc, Ratelimited):
            return Response({'error': 'Too many login attempts. Try again later.'},
                            status=status.HTTP_429_TOO_MANY_REQUESTS)
        return super().handle_exception(exc)

def logoutview(request):
    logout(request)
    return render(request, 'home_module/home.html')


def login(request):
    return render(request, 'account_module/login.html')


def signup(request):
    return render(request, 'account_module/signUp.html')


def profile(request):
    context = {
        'user': get_object_or_404(User, email=request.user.email)
    }
    return render(request, 'account_module/profile.html', context=context)
