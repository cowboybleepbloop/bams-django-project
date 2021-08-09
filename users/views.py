from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
def register(request):
    if request.method == 'POST': #checks to see if http post request
        form = UserRegisterForm(request.POST)
        if form.is_valid(): #if form is valid
            form.save() #saves the useras a new user
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created. Please login.') #to display the success message
            return redirect('login') #redirects to home page
    else:
      form = UserRegisterForm() #if not an http post request, gives the user a blank form
    return render(request, 'users/register.html', {'form': form})

@login_required #decorator makes login required to view profile
def profile(request):
    if request.method == 'POST': 
        u_form = UserUpdateForm(request.POST, instance=request.user)#populates form with info of current user
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid(): #chacks validation and saves forms
            u_form.save()
            p_form.save()
            messages.success(request, f'Account has been updated') #to display the success message
            return redirect('profile') #redirects user profile page
    else:
        u_form = UserUpdateForm(instance=request.user)#populates form with info of current user
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

