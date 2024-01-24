from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Coupon, UserProfile
from django import forms


class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = '__all__'


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'is_staff']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    ordering = ['email']


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    form = CouponForm
    list_display = ('code', 'is_valid', 'created_at', 'expires_at')
    list_filter = ('is_valid', 'created_at', 'expires_at')
    search_fields = ('code',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    # You can add custom validations or widgets here if needed


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'avatar')  # Customize as needed
    search_fields = ('user__email', 'user__first_name', 'user__last_name')