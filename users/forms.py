
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User
# , Patient, Doctor, Nurse
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
    }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Email"  



# This is the registeration form 
class UserRegistrationForm(UserCreationForm):
    
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']  # Set username to email
        if commit:
            # this is to save the user 
            user.save()
        return user



# class PatientRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Patient
#         fields = ('date_of_birth', 'blood_group', 'emergency_contact', 'address')
#         widgets = {
#             'date_of_birth': forms.DateInput(attrs={
#                 'type': 'date',
#                 'class': 'form-control'
#             }),
#             'blood_group': forms.TextInput(attrs={'class': 'form-control'}),
#             'emergency_contact': forms.TextInput(attrs={'class': 'form-control'}),
#             'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
#         }

# class DoctorRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Doctor
#         fields = ('specialization', 'license_number', 'department', 
#                  'consultation_fee', 'availability')
#         widgets = {
#             'specialization': forms.TextInput(attrs={'class': 'form-control'}),
#             'license_number': forms.TextInput(attrs={'class': 'form-control'}),
#             'department': forms.TextInput(attrs={'class': 'form-control'}),
#             'consultation_fee': forms.NumberInput(attrs={'class': 'form-control'}),
#         }

#     availability_days = forms.MultipleChoiceField(
#         choices=[
#             ('monday', 'Monday'),
#             ('tuesday', 'Tuesday'),
#             ('wednesday', 'Wednesday'),
#             ('thursday', 'Thursday'),
#             ('friday', 'Friday'),
#             ('saturday', 'Saturday'),
#             ('sunday', 'Sunday'),
#         ],
#         widget=forms.CheckboxSelectMultiple,
#         # required=True
#     )
    
#     time_start = forms.TimeField(
#         widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
#         # required=True
#     )
    
#     time_end = forms.TimeField(
#         widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
#         required=True
#     )

# class NurseRegistrationForm(forms.ModelForm):
#     SHIFT_CHOICES = (
#         ('morning', 'Morning'),
#         ('afternoon', 'Afternoon'),
#         ('night', 'Night'),
#     )
    
#     shift = forms.ChoiceField(
#         choices=SHIFT_CHOICES,
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )
    
#     class Meta:
#         model = Nurse
#         fields = ('department', 'shift')
#         widgets = {
#             'department': forms.TextInput(attrs={'class': 'form-control'}),
#         }