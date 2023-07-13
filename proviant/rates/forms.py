from django import forms
from .models import Rate


class RatesForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = '__all__'
