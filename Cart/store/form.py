from django import forms

from .models import RatingReview


class RatingReviewForm(forms.ModelForm):
    class Meta:
        model = RatingReview
        fields =['subject','review','rating']
