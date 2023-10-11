# forms.py
from django import forms
from .models import JobPost, JobCategory, CarouselSlider

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['job_category', 'post_name', 'post_image', 'whatsapp_phone', 'mobile_phone', 'website', 'city', 'post_description', 'is_approved']
        widgets = {
            'job_category': forms.Select(attrs={'class':'form-control'}),
            'post_name': forms.TextInput(attrs={'class': 'form-control'}),
            'post_image': forms.FileInput(attrs={'class':'form-control'}),
            'whatsapp_phone':forms.NumberInput(attrs={'class':'form-control'}),
            'mobile_phone':forms.NumberInput(attrs={'class':'form-control'}),
            'website':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'post_description': forms.Textarea(attrs={'class': 'form-control'}),
            'is_approved':forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                   }



class JobCategoryForm(forms.ModelForm):
    class Meta:
        model = JobCategory
        fields = '__all__'

        widgets = {
            
            'job_category_name': forms.TextInput(attrs={'class': 'form-control'}),
            'job_category_description': forms.Textarea(attrs={'class': 'form-control'}),
            # # 'is_active': forms.BooleanField(attrs={'class': 'form-control'}),
            # 'is_active': forms.BooleanField(attrs={'class': 'form-control'})
                   }
        


class AddSliderForm(forms.ModelForm):
    class Meta:
        model = CarouselSlider
        fields = '__all__'
        widgets = {
            
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image1': forms.FileInput(attrs={'class':'form-control'}),
            'image2': forms.FileInput(attrs={'class':'form-control'}),
            'image3': forms.FileInput(attrs={'class':'form-control'}),
            
                   }
        


from django import forms
from .models import VideshJobPost, NormalJobPost

class VideshJobPostForm(forms.ModelForm):
    class Meta:
        model = VideshJobPost
        fields = '__all__'
        widgets = {
            'job_category': forms.Select(attrs={'class':'form-control'}),
            'post_name': forms.TextInput(attrs={'class': 'form-control'}),
            'post_image': forms.FileInput(attrs={'class':'form-control'}),
            'whatsapp_phone':forms.NumberInput(attrs={'class':'form-control'}),
            'mobile_phone':forms.NumberInput(attrs={'class':'form-control'}),
            'website':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'post_description': forms.Textarea(attrs={'class': 'form-control'}),
            'is_approved':forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active':forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                   } 
        

class NormalJobPostForm(forms.ModelForm):
    class Meta:
        model = NormalJobPost
        fields = '__all__'

        widgets = {
            'job_category': forms.Select(attrs={'class':'form-control'}),
            'post_name': forms.TextInput(attrs={'class': 'form-control'}),
            'post_image': forms.FileInput(attrs={'class':'form-control'}),
            'whatsapp_phone':forms.NumberInput(attrs={'class':'form-control'}),
            'mobile_phone':forms.NumberInput(attrs={'class':'form-control'}),
            'website':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'post_description': forms.Textarea(attrs={'class': 'form-control'}),
            'is_approved':forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active':forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                   } 