from django.urls import path
from .views import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.loginfunc,name='login'),
    path('logout/',views.logoutfunc,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('',views.dashboard,name='dashboard'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='accounts/reset_password.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/reset_confirm.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_complete.html'),name='password_reset_complete'),
    path('change_password/',auth_views.PasswordChangeView.as_view(template_name='accounts/passwordchange.html'),name='password_change'),
    path('change_password_done',auth_views.PasswordChangeDoneView.as_view(template_name='accounts/passwordchangedone.html'),name='password_change_done'),
    
]
