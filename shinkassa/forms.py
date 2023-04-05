from django import forms

from .models import Worktable

class WorktableForm(forms.ModelForm):
    class Meta:
        model = Worktable
        fields = ['company', 'vehicle', 'number', 'diametr', 'complex', 'balance', 'count_gruz',
                  'sn', 'ust', 'mont', 'demont', 'appworks', 'cost_appworks'
                  ]