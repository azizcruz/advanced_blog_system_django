from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
import os
from django.conf import settings


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('blog:login_page')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html', {'form': form, 'title': 'Sign Up'})


@login_required
def profile(request):
    if request.method == 'POST':
        # Delete Previous Image To Avoid Duplicated Images Of Same User.
        if request.POST.get('image') != '':
            previous_image = os.path.join(settings.MEDIA_ROOT, request.user.profile.image.name)
            os.remove(previous_image)
        
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('users:profile_page')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'u': request.user,
        'title': f'{request.user.username} | Profile'
    }

    return render(request, 'users/profile.html', context)