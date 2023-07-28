from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


app_name = 'mvdm'
urlpatterns = [
    path('',views.index,name='index'),
    path('product/<int:id>/',views.detail,name='detail'),
    path('createproduct/',views.create_product,name='createproduct'),
    path('editproduct/<int:id>/', views.product_edit, name='editproduct'),
    path('delete/<int:id>/', views.product_delete, name='delete'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('register/',views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='mvdm/logout.html'),name='logout'),
    path('invalid/', views.invalid, name='invalid'),
    path('purchases/', views.my_purchases, name='purchases'),
    path('sales/', views.sales, name='sales'),
    path('order/',views.order, name='order'),

]