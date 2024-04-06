from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name ='crud'
urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('crud/', views.ProductListView.as_view(), name="list"),
    path('crud/create/', views.ProductCreateView.as_view(), name="create"),
    path('crud/detail/<int:pk>', views.ProductDetailView.as_view(), name="detail"),
    # path('crud/edit/<int:pk>', views.ProductUpdateView.as_view(), name="edit"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)