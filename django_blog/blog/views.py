from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.views import LoginView, LogoutView


class CustomLoginView(LoginView):
    template_name = 'blog/login.html'
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')  # or 'login'


class RegisterView(View):
    template_name = 'blog/register.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            # authenticate and log in the user
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            if user:
                login(request, user)
                messages.success(
                    request, "Registration successful. You're logged in.")
                return redirect('profile')  # or home
            return redirect('login')
        return render(request, self.template_name, {'form': form})


@login_required
def profile_view(request):
    # view profile
    return render(request, 'blog/profile.html', {'user': request.user})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        u = request.user
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=u.profile)
        # allow editing of email/first/last name via POST too
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if profile_form.is_valid():
            profile_form.save()
            if email:
                u.email = email
            if first_name is not None:
                u.first_name = first_name
            if last_name is not None:
                u.last_name = last_name
            u.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'blog/edit_profile.html', {
        'profile_form': profile_form,
        'user': request.user,
    })
