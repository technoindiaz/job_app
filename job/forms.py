# forms.py
from django import forms
from .models import JobPost

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['job_category', 'post_name', 'post_image', 'whatsapp_phone', 'mobile_phone', 'website', 'city', 'post_description']
        widgets = {
            'job_category': forms.Select(attrs={'class':'form-control'}),
            'post_name': forms.TextInput(attrs={'class': 'form-control'}),
            'post_image': forms.FileInput(attrs={'class':'form-control'}),
            'whatsapp_phone':forms.NumberInput(attrs={'class':'form-control'}),
            'mobile_phone':forms.NumberInput(attrs={'class':'form-control'}),
            'website':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'post_description': forms.Textarea(attrs={'class': 'form-control'}),
                   }
