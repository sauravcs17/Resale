from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.productlist, name='product_list'),

    path('postadd/', views.postadd, name='post_add'),

    path('<slug:category_slug>', views.productlist, name='product_list_category'),

    # path('<int:id>',views.productdetails,name='product_details')

    path('<slug:product_slug>/', views.productdetails, name='product_details'),
    path('<slug:product_slug>/delete/', views.delete, name='delete'),
    #path('details/goto/delete/', views.delete, name='delete'),


]
