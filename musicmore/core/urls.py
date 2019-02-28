from django.urls import path, include
from . import views


urlpatterns = [
    #paths de core
    #path('', views.home, name="home"),    
    path('', include('shop.urls'), name="shop"),
    path('cart/', include('cart.urls')),    
]