from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    photos = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    videos = forms.FileField(label='Select video files', widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Property
        fields = ['address', 'price', 'description', 'bedrooms', 'bathrooms', 'amenities', 'location']