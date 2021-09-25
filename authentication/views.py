
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from localStoragePy import localStoragePy
# Create your views here.
def Landing(request):
    return render(request,'landing.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/Login')
        
        
        # profile_obj = Profile.objects.filter(name = user_obj ).first()

        # if not profile_obj.is_verified:
        #     messages.success(request, 'Profile is not verified check your mail.')
        #     return redirect('/Login')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/Login')
        
        login(request , user)
        return redirect('/quiz')

    return render(request , 'Login.html')
    return render(request,'Login.html')


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
            profile_obj = Profile.objects.create(name = user_obj , auth_token = auth_token, password=password,email=email)
            p=Profile()
            p.name=name
            p.email=email
            p.password=password
            p.Year=Year
            p.save()
            print("aman")
            # send_mail_after_registration(email , auth_token)
            # print("3")
            # return redirect('/token')
            return render(request,'Login.html')
        except Exception as e:
            print(e)
    return render(request,'signup.html')
# def send_mail_after_registration(email , token):
#     print("akhil")
#     subject = 'Your accounts need to be verified'
#     message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
   
#     email_from = settings.EMAIL_HOST_USER
#     print(email_from)
#     recipient_list = [email]
#     print(recipient_list)
#     send_mail(subject, message , email_from ,recipient_list )
#     print(message)



#//////////////////////////////////////////////////////////////
def success(request):
    return render(request , 'success.html')


# def token_send(request):
#     return render(request , 'token.html')

# def verify(request , auth_token):
#     try:
#         profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    
#         if profile_obj:
#             if profile_obj.is_verified:
#                 messages.success(request, 'Your account is already verified.')
#                 return redirect('/Login')
#             profile_obj.is_verified = True
#             profile_obj.save()
#             messages.success(request, 'Your account has been verified.')
#             return redirect('/Login')
#         else:
#             return redirect('/error')
#     except Exception as e:
#         print(e)
#         return redirect('/signup')

def error_page(request):
    return  render(request , 'error.html')









@login_required(login_url='/Login')
def leadership(request):
    user=request.user
    print(user.username)
    return render(request,'leaderboard.html')
@login_required(login_url='/Login')
def quiz(request):
    # name=request.user.username
    # print(name)
    list=[]
    problems=McqProblems.objects.all()
    for i in problems:
        list.append(i)
    print(list)
    return render(request,'quizpage.html',{'list':list})

@login_required(login_url='/Login')
def Logout(request):
    logout(request)
    print("aman")
    #localStorage.setItem("type","")
    return HttpResponseRedirect('/')