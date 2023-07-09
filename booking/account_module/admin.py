from django.contrib import admin
from . import models
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone_number', 'is_active', 'is_staff', 'full_name', 'national_code', 'birth_date', 'address', 'is_superuser', 'gender']


admin.site.register(models.User,UserAdmin)