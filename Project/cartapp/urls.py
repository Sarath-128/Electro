
from django.urls import path
from . import views

urlpatterns = [
    path("viewcart/",views.view_cart,name="viewcart"),
    path("addcart/<int:id>",views.add_to_cart,name="addcart"),
    path("incr/<int:id>",views.increase_quantity,name="increase"),
    path("decr/<int:id>",views.decrease_quantity,name="decrease"),
    path("remove/<int:id>",views.remove_cart,name="remove"),
    path("payment/",views.Payment,name="payment"),
    path("success/",views.Success,name="success"),
    path("cancel/",views.Cancel,name="cancel"),

]