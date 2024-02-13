from django.shortcuts import render, redirect
from .forms import FeedbackForm


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
    return render(request, 'about.html')
