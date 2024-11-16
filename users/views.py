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

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                # return render(request, 'base.html',{'form': form})
                redirect("users:profile")
            else:
                messages.error(request, 'Authentication failed.')
        else:
            print(f"Login form errors: {form.errors}")
            messages.error(request, 'Invalid email  or password.')
    else:
        form = UserLoginForm()
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
    # profile = None 
    return render(request,  {
        'user': user,
        # 'profile': profile
    })