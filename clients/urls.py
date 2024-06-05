from django.urls import path
from clients.views import login,dashboard,logout,create

app_name='clients'

urlpatterns = [
    path('login',login,name="login"),
    path('logout',logout,name='logout'),
    path('dashboard',dashboard,name='dashboard'),
    path('create',create,name='create'),

]