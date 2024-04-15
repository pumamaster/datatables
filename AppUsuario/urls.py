from django.urls import path
from .views import LoginView, LogoutView, RegistrarView, ListaUsuarioView, UsuarioUpdateView,UsuarioDeleteView


urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='loginview'),
    path('logout/', LogoutView.as_view(), name='logoutview'),
    path('registrar-usuario/', RegistrarView.as_view(), name='registrarview'),
    path('usuariolist/', ListaUsuarioView.as_view(), name='usuariolist'),
    path('usuarioedit/', UsuarioUpdateView.as_view(), name='usuarioedit'),
    path('usuariodelete/<int:pk>', UsuarioDeleteView.as_view(), name='usuariodelete'),
]