
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from .models import User
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token


class API_SignUp(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

def auth_login(request, user):
    pass


class API_Login(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(email__iexact=email).first()
        if user:
            pas = user.check_password(password)
            if pas:
                auth_login(request, user)
                user.last_login = timezone.now()
                user.save()
                return Response({'msg': 'successful'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
def login(request):
    return render(request, 'account_module/login.html')


def signup(request):
    return render(request, 'account_module/signUp.html')
