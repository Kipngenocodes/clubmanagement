from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('Login/', views.login_student, name='login'),
    # path('Logout/', views.logout_student, name='Logout'),


]
