from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.models import User
# from django import forms
from .models import Post, Category
from django.forms import ModelForm

class LoginForm(AuthenticationForm):
    class Meta:
        fields = ('username', 'password')
        labels = {
            'username': 'Username:',
            'passsword': 'Password:',
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder': '@username'})
        self.fields['password'].widget.attrs.update({'class':'form-control', 'title': 'if not, I cant help you', 'placeholder': 'Do you remember your Password'})
        
        
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = {'cat_name'}
        labels = {
            'cat_name': 'Name the Category:'
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat_name'].widget.attrs.update({'class':'form-control', 'placeholder': 'What is the name?'})

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'excerpt', 'content')#, 'featured_image')
        labels = {
            'title': 'Title:',
            'category':'Category (Group)',
            'excerpt': 'Brief Description (excerpt):',
            'content': 'Body (content):'
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control', 'placeholder': 'What is the name?'})
        self.fields['category'].widget.attrs.update({'class':'form-control', 'placeholder': 'What is the category?'})
        self.fields['excerpt'].widget.attrs.update({'class':'form-control', 'placeholder': 'A simple highlight'})
        self.fields['content'].widget.attrs.update({'class':'form-control', 'placeholder': 'The whole story'})
        
        