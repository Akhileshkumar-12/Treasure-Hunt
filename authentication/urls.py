
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Landing, name="landing"),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('leadership',views.leadership,name="leadership"),
    # a///////////////////////////////////////////////////////////////////
    path('token' , views.token_send , name="token_send"),
    path('success' , views.success , name='success'),
    path('verify/<auth_token>' , views.verify , name="verify"),
    path('error' , views.error_page , name="error")
    
]
