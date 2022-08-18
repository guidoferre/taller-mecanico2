from operator import setitem
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from blog import views
from blog.views import inicio
from blog.views import cliente
from django.urls import include
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)