from django import forms
from .models import Trip

class TripForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Trip
        fields = ['destination', 'start_date', 'end_date', 'notes']
