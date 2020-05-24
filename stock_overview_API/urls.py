"""stock_overview_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from preserial_stock import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('customers/', views.ShowAllCustomersView.as_view(), name='customers_list'),
    path('customer/<int:id>', views.ShowProjectsView.as_view(), name='projects_list'),
    path('project/<int:id>', views.ShowProductsView.as_view(), name='product_list'),
    path('product/<int:id>', views.ShowDetailProductsView.as_view(), name='product_detail_list'),
    path('create_customer/', views.CreateCustomerNameView.as_view(), name='create_customer'),
    path('create_project/', views.CreateProjectNameView.as_view(), name='create_project'),
    path('create_final_product/', views.CreateFinalProductNumberView.as_view(), name='create_final_product'),
    path('create_single_products/', views.CreateSingleProductsNumberView.as_view(), name='create_single_products'),

]
