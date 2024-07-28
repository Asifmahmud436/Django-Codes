from django.contrib import admin
from .models import UserAddress,UserBankAccounts
# Register your models here.

admin.site.register(UserBankAccounts)
admin.site.register(UserAddress)
