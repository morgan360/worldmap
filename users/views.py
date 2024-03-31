from django.shortcuts import render, redirect
from users.forms import CouponSignupForm, UserProfileForm, CustomLoginForm
from .models import Coupon
from django.db import transaction
from django.contrib import messages
from .models import Coupon, CustomUser, UserProfile
from django.contrib.auth.decorators import login_required


def my_signup_view(request):
    print("my_signup_view")
    if request.method == 'POST':
        form = CouponSignupForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                coupon_code = form.cleaned_data.get('coupon_code')
                if coupon_code:
                    try:
                        coupon = Coupon.objects.get(code=coupon_code, is_valid=True)
                        if coupon.expires_at and coupon.expires_at < timezone.now():
                            messages.error(request, "This coupon has expired.")
                            return render(request, 'account/signup.html', {'form': form})
                        else:
                            user = form.save(request)
                            coupon.user = user
                            coupon.is_valid = False
                            coupon.save()
                            messages.success(request, "Coupon applied successfully.")
                            return redirect('account_login')
                    except Coupon.DoesNotExist:
                        messages.error(request, "Invalid coupon code.")
                        return render(request, 'account/signup.html', {'form': form})
                else:
                    # Handle case when no coupon code is provided
                    user = form.save(request)
                    messages.success(request, "Signup successful.")
                    return redirect('account_login')
        else:
            messages.error(request, form.errors)

    else:
        form = CouponSignupForm()

    return render(request, 'account/signup.html', {'form': form})


@login_required
def view_profile(request):
    return render(request, 'profile.html', {'user': request.user})


# Update Profile Form


def update_profile(request):
    user = request.user
    try:
        profile = user.profile
    except UserProfile.DoesNotExist:
        UserProfile.objects.create(user=user)
        profile = user.profile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')  # Adjust the redirect as needed
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'update_profile.html', {'form': form})


def my_login_view(request):
    print("my_login_view")
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = CustomLoginForm()

    return render(request, 'account/login.html', {'form': form})
