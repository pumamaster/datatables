from django.contrib import admin 
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('datatables/', include('AppDatatables.urls')),
    path('usuario/', include('AppUsuario.urls')),
]
