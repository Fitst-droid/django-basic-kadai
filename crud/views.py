from django.shortcuts import render
from django.views.generic import  ListView, DetailView, TemplateView
from django.views.generic.edit import  CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Product

class TopView(TemplateView):
  template_name = 'top.html'

class ProductCreateView(CreateView):
  model = Product
  fields = '__all__'
  success_url = reverse_lazy('list') 

class ProductListView(ListView):
  template_name = 'list.html'
  model = Product
  paginate_by = 4

class ProductDetailView(DetailView):
  model = Product
  fileds = '__all__'
  success_url = reverse_lazy('list')

# class ProductUpdateView(UpdateView):
#   model = Product
#   fileds = '__all__'
#   template_name_suffix = '_updete_form.html'
#   success_url = reverse_lazy('crud_list')
