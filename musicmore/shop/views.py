from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q



# Create your views here.
class ShopListView(ListView):
    model = Product
    template_name = 'shop/product_list.html'
    paginate_by = 4

    def get_queryset(self):
        new_context = Product.objects.all()
        if 'search' in self.request.GET:
            filter_val = self.request.GET.get('search', 'give-default-value')        
            new_context = Product.objects.filter(Q(name__contains=filter_val) | Q(description__contains=filter_val))
        return new_context

    def get_context_data(self, **kwargs):
        context = super(ShopListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('search', 'give-default-value')        
        return context

class ShopDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'

    def get_object(self):
        return get_object_or_404(Product, name=self.kwargs['name'])