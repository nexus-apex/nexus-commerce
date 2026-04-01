from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('shopproducts/', views.shopproduct_list, name='shopproduct_list'),
    path('shopproducts/create/', views.shopproduct_create, name='shopproduct_create'),
    path('shopproducts/<int:pk>/edit/', views.shopproduct_edit, name='shopproduct_edit'),
    path('shopproducts/<int:pk>/delete/', views.shopproduct_delete, name='shopproduct_delete'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/<int:pk>/edit/', views.order_edit, name='order_edit'),
    path('orders/<int:pk>/delete/', views.order_delete, name='order_delete'),
    path('shopcategories/', views.shopcategory_list, name='shopcategory_list'),
    path('shopcategories/create/', views.shopcategory_create, name='shopcategory_create'),
    path('shopcategories/<int:pk>/edit/', views.shopcategory_edit, name='shopcategory_edit'),
    path('shopcategories/<int:pk>/delete/', views.shopcategory_delete, name='shopcategory_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
