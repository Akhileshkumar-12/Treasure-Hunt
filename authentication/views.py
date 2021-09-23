
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.
def Landing(request):
    return render(request,'landing.html')
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        Year= request.POST.get('year')
        print(password)
        try:
            if User.objects.filter(username = name).first():
                messages.success(request, 'Username is taken.')
                return redirect('/signup')
            print("1")
            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/signup')
            print("2")
            user_obj = User(username = name , email = email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(name = user_obj , auth_token = auth_token)
            profile_obj.save()
            
            send_mail_after_registration(email , auth_token)
            print("3")
            return redirect('/token')
           
        except Exception as e:
            print(e)
    return render(request,'signup.html')
def send_mail_after_registration(email , token):
    print("akhil")
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
   
    email_from = settings.EMAIL_HOST_USER
    print(email_from)
    recipient_list = [email]
    print(recipient_list)
    send_mail(subject, message , email_from ,recipient_list )
    print(message)

















#//////////////////////////////////////////////////////////////
def success(request):
    return render(request , 'success.html')


def token_send(request):
    return render(request , 'token.html')

def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    
        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/signup')

def error_page(request):
    return  render(request , 'error.html')









def login(request):
    return render(request,'login.html')
def leadership(request):
    return render(request,'leaderboard.html')