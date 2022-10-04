from django.contrib import admin
from django.urls import path, include
from biblioteca.home_view import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livro/', include('livro.urls')),
    path('auth/', include('usuarios.urls')),
    path('', home)
]
