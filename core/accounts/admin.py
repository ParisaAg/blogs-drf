from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile
from django import forms
# Register your models here.




class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'first_name', 'is_active', 'is_superuser']
    search_fields =  ['email', 'first_name', 'is_active', 'is_superuser']
    ordering = ['email']
    fieldsets = (
        ('Authentication', {
            'fields': 
            ('email', 'password',)
        }),
        ('permissions', {
            'fields': 
            ('is_staff','is_active', 'is_superuser')
            
        }),
        ('group_permissions',{
            'fields':
            ('groups','user_permissions')
        }),
        ('important_date',{
            'fields':
            ('last_login',)
        }
        )
    )




    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_superuser')
        }),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)