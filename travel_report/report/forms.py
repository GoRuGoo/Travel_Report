from .models import TravelReport
from django import forms

class ReportCreateForm(forms.ModelForm):
    class Meta:
        model = TravelReport
        fields = ('user','title',
        'transportation','cost','member','thoughts')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'