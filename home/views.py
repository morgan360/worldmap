from django.shortcuts import render, redirect
from django.views.generic import FormView

from .forms import FeedbackForm, ContactForm, CustomLoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail  # Import Django's send_mail function
from .models import ContactSubmission  # Import your model


def home(request):
    if request.user.is_authenticated:
        # Redirect to a different page or render a different template for logged-in users
        return render(request, 'logged_in_home.html')
    else:
        # Render the regular homepage template for non-logged-in users
        return render(request, 'home.html')


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('success_page')  # Redirect to a success page or elsewhere
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})


def about(request):
    form = ContactForm()
    return render(request, 'about.html', {'form': form})


def submit_contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            contact_submission = ContactSubmission.objects.create(
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )

            # Optionally, send an email or perform other actions

            # Redirect to a new URL:
            return HttpResponseRedirect(reverse('contact_thanks'))
    else:
        form = ContactForm()

    return render(request, 'admin.html', {'form': form})


def thanks_view(request):
    # Render the 'contact_thanks.html' template
    return render(request, 'contact_thanks.html')


class CustomLoginView(FormView):
    form_class = CustomLoginForm
    success_url = 'users'  # or where you want to redirect after login
    template_name = 'account/login.html'  # path to your login template