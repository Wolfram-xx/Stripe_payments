"""
URL configuration for StripePayments project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from Payments.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('home/', index_page),
    path('create/', create_page),
    path('create_item/', create_item),
    path('item/<int:item_id>/', item_page),
    path('buy/<int:item_id>', buy_item),
    path('add_to_order/<int:item_id>', add_to_order),
    path('order/', order_page),
    path('delete_from_order/<int:item_id>', delete_from_order),
    path('buy_order/<int:order_id>', buy_order),
    path('currency_error/', currency_error_page),
]
