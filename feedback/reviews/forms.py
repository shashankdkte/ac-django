from django import forms

class ReviewForm(forms.Form):
  user_name = forms.CharField(label="Your username", max_length=100, error_messages={
    "required":"Your name cannot be empty",
    "max_length":"Please enter a shorter name"
  })
  review_text = forms.CharField(label="Your Feedback",widget=forms.Textarea,max_length=200)
  rating = forms.IntegerField(label="Your rating",min_value=1,max_value=5)
