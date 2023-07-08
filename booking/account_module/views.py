from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from .models import User
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as auth_login

@login_required
def API_Profile(request):
    print('45')
    if request.method == 'POST':
        user = request.user
        # user.full_name = request.POST.get('full_name', '')
        user.email = request.POST.get('email', '')
        user.phone_number = request.POST.get('phone_number', '')
        # user.address = request.POST.get('address', '')
        # user.birth_date = request.POST.get('birth_date', '')

        user.save()
        return JsonResponse({"success": True, "message": "مشخصات کاربری با موفقیت به‌روز شد."})
    else:
        return JsonResponse({"success": False, "message": "خطا: درخواست نامعتبر."})

# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def API_Profile(request):
#     user = request.user
#     email = request.data.get('email')
#     phone_number = request.data.get('phone_number')
#     print(email)
#     print(phone_number)
#     # بررسی تکراری نبودن ایمیل و شماره تلفن
#     if email and email != user.email and User.objects.filter(email=email).exists():
#         return Response({'error': 'This email address is already in use.'}, status=status.HTTP_400_BAD_REQUEST)
#     if phone_number and phone_number != user.phone_number and User.objects.filter(phone_number=phone_number).exists():
#         return Response({'error': 'This phone number is already in use.'}, status=status.HTTP_400_BAD_REQUEST)
#
#     serializer = UserSerializer(user, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#

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
                print(request.user.is_authenticated)
                return Response({'msg': 'successful'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


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
