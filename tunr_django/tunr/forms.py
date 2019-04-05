from django import forms
from .models import Artist, Song


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('name', 'nationality', 'photo_url',)
