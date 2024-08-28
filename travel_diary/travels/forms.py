from django import forms
from .models import TravelEntry

class TravelEntryForm(forms.ModelForm):
    class Meta:
        model = TravelEntry
        fields = ['title', 'description', 'location', 'image', 'cost', 'convenience_rating', 'safety_rating', 'population_density_rating', 'vegetation_rating']
