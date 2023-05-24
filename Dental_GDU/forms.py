from django import forms
from .models import Person
from .models import Note

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['nume', 'varsta', 'email']


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['content']
