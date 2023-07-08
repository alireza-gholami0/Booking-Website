from django.shortcuts import render, get_object_or_404

from account_module.models import User


# Create your views here.
def home(request):
    context = {
        'user': get_object_or_404(User, email=request.user.email)
    }
    return render(request, 'home_module/home.html', context)