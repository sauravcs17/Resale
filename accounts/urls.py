"""tels URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . views import register
from django.contrib.auth import views as auth_views
from . import views
app_name = 'accounts'

urlpatterns = [
     path('register/' ,views.register ,name='register') , 
     path('login/', views.login, name='login'),
     path('profile/', views.profile, name='profile'),
     path('password_change/' , auth_views.PasswordChangeView.as_view() , name='password_change') , 
     path('password_change/done/' , auth_views.PasswordChangeDoneView.as_view() , name='password_change_done') , 
     path('password_reset/' , auth_views.PasswordResetView.as_view() , name='password_reset') , 
     path('password_reset/done/' , auth_views.PasswordResetDoneView.as_view() , name='password_reset_done') , 

]
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']
