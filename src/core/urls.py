from django.urls import path
from .views import item_list, show_checkout


urlpatterns = [
    path('', item_list, name="list-of-items"),
    path('checkout/', show_checkout, name="checkout_page")
]
