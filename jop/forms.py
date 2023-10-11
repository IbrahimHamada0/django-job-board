from django import forms
from .models import *


class ApllyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = '__all__'
        exclude = ['created_at', 'job']
        
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('owner','slug')        
