from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . models import Question, Response
from django import forms


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']



class LoginForm(AuthenticationForm):
    class Meta:
        fields = "__all__"        


class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title','body']       



class NewResponseForm(forms.ModelForm):
    class Meta:
        model = Response 
        fields = ['body']  

class NewReplyForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['body'] 
        widgets = {
           'body': forms.Textarea(attrs={
               'rows': 2,
                'placeholder':'what are your thoughts'
             })


        }        