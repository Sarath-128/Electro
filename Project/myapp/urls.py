
from django.urls import path
from . import views

urlpatterns = [
    path("dash/",views.Pro_Details,name="dash"),
    path("create/",views.CreateProduct,name='create'),
    path('update/<int:id>/',views.Pro_Update,name="update"),
    path("del/<int:id>/",views.Pro_Delete,name="delete"),
    path('search/',views.Pro_Search,name="adminSearch"),
    path('notfound/',views.notfound,name="notfound"),
    path('test/',views.test,name='test')
]