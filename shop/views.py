from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Product


class ProductListView(generic.ListView):
    model = Product
    template_name = 'shop/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        active_product = self.model.objects.filter(active=True)
        return active_product


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'shop/product_detail.html'


class ProductCreateView(generic.CreateView):
    model = Product
    fields = ['title', 'description', 'price', 'active']
    template_name = 'shop/product_create.html'


class ProductUpdateView(generic.UpdateView):
    model = Product
    fields = ['title', 'description', 'price', 'active']
    template_name = 'shop/product_update.html'


class ProductDeleteView(generic.DeleteView):
    model = Product
    template_name = 'shop/product_delete.html'
    success_url = reverse_lazy('home')
