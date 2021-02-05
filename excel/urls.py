"""excel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,reverse_lazy
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import RedirectView
from api.views import CountryAutocomplete,ObjectAutocomplete,TypeAutocomplete


urlpatterns = [
    path('api/',include('api.urls')),
    path('', RedirectView.as_view(url=reverse_lazy('index'))),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    #path('tinymce/', include('tinymce.urls')),
    path('jet/', include('jet.urls', 'jet')),
    #path('grappelli/', include('grappelli.urls')),  # Django JET URLS
    path('admin/', admin.site.urls),
    url(
        r'^country-autocomplete/$',
        CountryAutocomplete.as_view(),
        name='country-autocomplete',
    ),
    url(
        r'^object-autocomplete/$',
        ObjectAutocomplete.as_view(),
        name='object-autocomplete',
    ),
    url(
        r'^type-autocomplete/$',
        TypeAutocomplete.as_view(),
        name='type-autocomplete',
    ),
    
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
