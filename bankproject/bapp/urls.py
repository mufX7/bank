from django.urls import path

from bapp import views, admin

app_name='BankingApp'
urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('loginsuccess/',views.loginsuccess,name='loginsuccess'),
    path('last/',views.last,name='last'),
    path('form/',views.form,name='form')
]