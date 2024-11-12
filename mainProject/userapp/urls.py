from django.urls import path
from . import views

urlpatterns = [
    path("testing/",views.test,name="testing"),
    path("",views.UserTest,name="home"),
    path("store/",views.Store,name="store"),
    path("checkout/<int:id>/",views.Checkout,name="checkout"),
    path("sea/",views.Search,name="searchuser"),
    path("login/",views.Login,name="login"), 
    path("register/",views.Register,name="register"),
    path("out/",views.Logout,name="logout"),
]