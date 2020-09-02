"""olx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from auctions import views as auctions_views

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('products/', include('product.urls',namespace='products')),
    #path('Auction/',include('productauction.urls',namespace='productauction')),
    path('index/', auctions_views.index, name="index"),
    path('myauctions/', auctions_views.my_auctions, name="my_auctions"),

    path('myauctions/<int:auction_id>/bidderlist/',auctions_views.bidderslist, name="bidlist"),

   


    path('mybids/', auctions_views.my_bids, name="my_bids"),
    path('auctions/', include('auctions.urls',namespace='auction')),
    path('accounts/', include('accounts.urls', namespace='accounts')),




]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
