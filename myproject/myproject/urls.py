from django.contrib import admin
from django.urls import path
from crud import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Top.as_view()),
    path('crud/', views.ProductListView.as_view(), name="list"),
    path('crud/detail/<int:pk>', views.ProductDetailView.as_view(), name="detail"),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  