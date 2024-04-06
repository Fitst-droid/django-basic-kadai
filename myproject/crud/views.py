from django.shortcuts import render
from django.views.generic import  ListView, DetailView, TemplateView, CreateView
from django.urls import reverse_lazy
from .models import Product

class Top(TemplateView):
  template_name = 'top.html'

class ProductCreateView(CreateView):
  template_name = "create.html"
  success_url = reverse_lazy('list') 

class ProductListView(ListView):
  model = Product
  template_name ="list.html"
  paginate_by = 4

class ProductDetailView(DetailView):
  model = Product
  filed = '__All__'