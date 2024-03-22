from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming you have a User model
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5 rating
    comment = models.TextField()

    def __str__(self):
        return f"Feedback by {self.user.email}"


class ContactSubmission(models.Model):
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact from {self.email} on {self.submitted_at}"
