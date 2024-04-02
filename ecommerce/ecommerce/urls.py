"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings             # these two path must import for settings.DEBUG (media content view)
from django.conf.urls.static import static   # for settings.DEBUG (media content view)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('search/', include('cart.urls')),
    path('cart/', include('search.urls')),
]
if settings.DEBUG:                                          #for viewing content inside media in website add this settings.DEBUG
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
