from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_lesson1.urls')),
    path('lesson2/', include('app_lesson2.urls')),  
]  

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)