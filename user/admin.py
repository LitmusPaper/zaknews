from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import MyUser

class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': (
        'first_name', 'last_name', 'email', 'bio')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    '''
    fieldsets = UserAdmin.fieldsets + ((None, {'fields':('bio',)}),)
    '''
admin.site.register(MyUser, MyUserAdmin)