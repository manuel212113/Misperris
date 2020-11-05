from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
import include



urlpatterns = [
    path('', views.paginaInicio, name='paginaInicio'),
    path('contacto.html', views.contacto, name='contacto'),
    path('index.html', views.paginaInicio, name='paginaInicio'),
    path('rescatados.html', views.mostrarRescatados  , name='rescatados'),
    path('registro', views.RegistroUsuario, name='RegistroUsuario'),
    path('login',  LoginView.as_view(template_name='login.html') , name='login'),
    path('logout', LogoutView.as_view(template_name='index.html'), name='logout'),
    path('reset', auth_views.PasswordResetView.as_view(), name='reset'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_confirm/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    


]