from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm): # UserForm 클래스는 UserCreationForm 클래스를 상속받는다.
    email = forms.EmailField(label="Email") # email 필드를 추가한다.

    class Meta: # Meta class는 UserForm 클래스에 대한 정보를 제공한다.
        model = User # User model을 사용하겠다.
        fields = ("username", "password1", "password2", "email") # User model의 필드 중에서 사용할 필드를 지정한다.
