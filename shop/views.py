from django.shortcuts import render
from django.views import generic

from .models import Product


class ProductListView(generic.ListView):
    model = Product
    template_name = 'shop/product_list.html'


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

