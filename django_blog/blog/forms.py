from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # author and published_date set automatically / by view
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your post here...', 'class': 'form-control', 'rows': 10}),
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True, help_text="Required. Enter a valid email address.")
    first_name = forms.CharField(required=False, max_length=30)
    last_name = forms.CharField(required=False, max_length=30)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "A user with that email already exists.")
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # if you removed avatar from model, remove it here too
        fields = ('bio', 'avatar')
