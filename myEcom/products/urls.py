from django.urls import path, include

from products import views

urlpatterns = [
     path('latest-products/', views.LatestProductsList.as_view(), name='latest-products'),
    path('products/search/', views.search, name='product-search'),
    path('products/dashboard/', views.DashboardView.as_view(), name='dashboard')
]