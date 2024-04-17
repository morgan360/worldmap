from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from .models import CustomUser, Coupon, UserProfile

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'first_name', 'handle', 'is_active', 'is_staff']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'handle')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'handle'),
        }),
    )
    search_fields = ('email', 'first_name', 'handle')
    ordering = ['email']

class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = '__all__'

class CouponAdmin(admin.ModelAdmin):
    form = CouponForm
    list_display = ('code', 'is_valid', 'created_at', 'expires_at')
    list_filter = ('is_valid', 'created_at', 'expires_at')
    search_fields = ('code',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'
    fk_name = 'user'

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'avatar')
    search_fields = ('user__email', 'user__first_name', 'user__handle')

# Register the admin models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
