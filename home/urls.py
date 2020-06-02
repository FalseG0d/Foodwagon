from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('request',views.make_request,name="make_request"),
    path('register',views.register,name="register"),
    path('login',views.loginUser,name="login"),
    path('logout',views.logoutUser,name="logout"),
]
