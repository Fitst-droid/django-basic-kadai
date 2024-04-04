from django.shortcuts import render
from django.views.generic import  ListView, DetailView, TemplateView
from .models import Product

class Top(TemplateView):
  template_name = 'top.html'

class ProductListView(ListView):
  model = Product
  template_name ="list.html"
  paginate_by = 4

class ProductDetailView(DetailView):
  model = Product
  filed = '__All__'