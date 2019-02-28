from django.urls import path, include
from .views import ShopListView, ShopDetailView

app_name='shop'

urlpatterns = [
    #paths de core
    path('', ShopListView.as_view(), name='list'),   
    path('/<name>/', ShopDetailView.as_view(), name='detail'),
]