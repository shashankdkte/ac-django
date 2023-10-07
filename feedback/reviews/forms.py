from django import forms

class ReviewForm(forms.Form):
  username = forms.CharField(label="Your username", max_length=100, error_messages={
    "required":"Your name cannot be empty",
    "max_length":"Please enter a shorter name"
  })

