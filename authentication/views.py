
from django.core import paginator
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
# from localStoragePy import localStoragePy
from django.core.paginator import Paginator
import datetime

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

    return render(request , 'login.html')
    # return render(request,'Login.html')


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
            # p=Profile()
            # p.name=request.user.username
            # p.email=email
            # p.password=password
            # p.Year=Year
            profile_obj.save()
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
    # p=Profile.objects.get(name=user)
    # score=p.score
    p=Profile.objects.all()
    p=p.order_by('-score')
    j=1
    myscore=0
    myrank=1
    for i in p:
        i.id=j
        j+=1
        if i.name==user:
            myrank=i.id
            myscore=i.score
    print(myscore)
    for i in p:
        print(i.name.username)
    return render(request,'leaderboard.html',{'list':p,'myrank':myrank,'myscore':myscore})
@login_required(login_url='/Login')
def quiz(request):
    # name=request.user.username
    # print(name)
    user=request.user
    p=Profile.objects.get(name=user)
    k=p.is_verified
    if k==True:
        return render(request,'finish.html')
    p.is_verified=True
    #p.name=user
    p.save()
    problems=McqProblems.objects.all()
    paginator=Paginator(problems,1)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    print(page_number)
    print(page_obj)
    ob=Event.objects.all()
    today=datetime.datetime.now()
    print(today)
    # obj1=Event()
    # for i in ob:
    #     obj1=i
    #     break
    # print(obj1)
    for i in ob:
        today=i.When
        break
    print('aman')
    print(today)
    #return render(request,'jaya.html',{'ob':ob})
    # for i in problems:
    #     list.append(i)
    # print(list)
    return render(request,'quizpage.html',{'page_obj':page_obj,'page_number':page_number,'ob':today})

@login_required(login_url='/Login')
def Logout(request):
    logout(request)
    print("aman")
    #localStorage.setItem("type","")
    return HttpResponseRedirect('/')
def score(request,pk):
    #print('aman')
    if request.method=='POST':

        op1=request.POST['1']
        print('selcted an',op1)
        problems=McqProblems.objects.all()
        op1=int(op1)
        count=0
        user=request.user
        m=McqSubmissions()
        p=Profile.objects.get(name=user)
        if(pk=='None'):
            count=1
        else:
            count=int(pk)
        l=0
        for i in problems:
            l=l+1
            if count==l:
                m.question=i
                verify=McqSubmissions.objects.filter(question=i)
                if verify:
                    return render(request,'finish.html')
                m.submitted_output=op1 
                if op1==i.correct_ans :
                    m.result=True
                    d=p.score
                    p.score=d+1
                else:
                    m.result=False
        p.save()
        m.user=p
        m.save()
    
    if(pk=='None'):
        pk='2'
    else:
        pk=int(pk)+1
        pk=str(pk)
    problems=McqProblems.objects.all()
    paginator=Paginator(problems,1)
    l=problems.__len__()
    # print(l)
    k=int(pk)
    # print(k)
    if l<k:
        p=Profile.objects.get(name=user)
        print('score')
        print(p.score)
        return render(request,'finish.html')
    #paginator=Paginator(problems,1)
    page_obj=paginator.get_page(pk)
    ob=Event.objects.all()
    today=datetime.datetime.now()
    print(today)
    # obj1=Event()
    # for i in ob:
    #     obj1=i
    #     break
    # print(obj1)
    for i in ob:
        today=i.When
        break
    print('aman')
    print(today)
    #print(pk)
    print(page_obj)
    # for i in problems:
    #     list.append(i)
    # print(list)
    return render(request,'quizpage.html',{'page_obj':page_obj,'page_number':pk,'ob':today})

def finish(request):
    return render(request,'finish.html')