from django import forms
from .models import Song
from .models import Comment

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('title', 'artist', 'genre', 'audio_file')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)