from django.shortcuts import render, HttpResponse

# Create your views here.
# Create your views here.
def home(request):
    #return render(request, "shop/shop.html")
    return render(request, "core/home.html")