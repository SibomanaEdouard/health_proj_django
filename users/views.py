from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .models import User
from .forms import (
    UserLoginForm, UserRegistrationForm, 
    # PatientRegistrationForm, DoctorRegistrationForm, NurseRegistrationForm
)

# def login_view(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             print("The form is valid")
#             user = form.get_user()
#             print("The user is ", user)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, 'Login successful!')
#                 # Redirect based on user type
#                 if user.user_type == 'user':
#                     return redirect('base')
#                 elif user.user_type == 'patient':
#                     return redirect('patient_dashboard')
#                 elif user.user_type == 'doctor':
#                     return redirect('doctor_dashboard')
#                 elif user.user_type == 'nurse':
#                     return redirect('nurse_dashboard')
#                 else:
#                     return redirect('admin_dashboard')
#             else:
#                 messages.error(request, 'Authentication failed.')
#         else:
#             print(f"Login form errors: {form.errors}")
#             messages.error(request, 'Invalid email  or password.')
#     else:
#         form = UserLoginForm()
#     return render(request, 'users/login.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        print("Logging in ")
        print("This is the form data : ",form)
        if form.is_valid ():
            print("Form is valid")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blogs:home')  # Replace 'home' with your desired redirect URL
    else:
        form = UserLoginForm()
        print("Failed to login , you sent invalid form ")
    return render(request, 'users/login.html', {'form': form})


# this is to the register view 
@transaction.atomic
def register_view(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            try:
                with transaction.atomic():
                    # Create user but don't save the password yet
                    user = user_form.save(commit=False)
                    user.username = user_form.cleaned_data['email']  # Set username to email
                    user.email = user_form.cleaned_data['email']
                    
                    # Set the password properly
                    user.set_password(user_form.cleaned_data['password1'])
                    user.save()
                    messages.success(request, 'Registration successful! Please login.')
                    return redirect('users:login')
            
            except Exception as e:
                messages.error(request, f'Registration failed: {str(e)}')
                # Rollback will happen automatically due to @transaction.atomic
                return redirect('users:register')
        else:
            # If forms are invalid, collect all errors
            for field, errors in user_form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        user_form = UserRegistrationForm()
        
    context = {
        'user_form': user_form,
        # 'patient_form': PatientRegistrationForm(),
        # 'doctor_form': DoctorRegistrationForm(),
        # 'nurse_form': NurseRegistrationForm(),
    }
    
    return render(request, 'users/register.html', context)


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('users:login')

@login_required
def profile_view(request):
    user = request.user
    profile = None
    
    if user.user_type == 'patient':
        profile = user.patient_profile
    elif user.user_type == 'doctor':
        profile = user.doctor_profile
    elif user.user_type == 'nurse':
        profile = user.nurse_profile
    
    return render(request, 'users/profile.html', {
        'user': user,
        'profile': profile
    })