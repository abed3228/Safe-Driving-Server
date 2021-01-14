from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate, update_session_auth_hash
#from .forms import TodoForm,DeviceForm,TapForm
#from .models import Todo,Blog,Devices,Status,Tap
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponse
from django.contrib import messages 
#from .forms import SignUpForm, EditProfileForm

# Create your views here.

def home(request):
    return render(request,'website/ComingSoon.html')