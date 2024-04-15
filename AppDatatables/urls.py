from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'articulos', ArticuloViewSet, basename='articulo')
router.register(r'articuloindividual', ArticuloIndividualViewSet, basename='articuloindividual')
router.register(r'eventos', EventoViewSet, basename='evento')
router.register(r'partidos', PartidoViewSet, basename='partido')
router.register(r'fotodia', FotoDiaViewSet, basename='fotodia')
router.register(r'logo', LogoViewSet, basename='logo')
router.register(r'cartas', CartaViewSet, basename='carta')

urlpatterns = [
    path('', ArticuloListView.as_view(), name='articulolist'),
    path('articulocreate/', ArticuloCreateView.as_view(), name='articulocreate'),
    path('articuloupdate/<int:pk>', ArticuloUpdateView.as_view(), name='articuloupdate'),
    path('articulodetail/<int:pk>', ArticuloDetailView.as_view(), name='articulodetail'),

    path('eventolist/', EventoListView.as_view(), name='eventolist'),
    path('eventocreate/', EventoCreateView.as_view(), name='eventocreate'),
    path('eventoupdate/<int:pk>', EventoUpdateView.as_view(), name='eventoupdate'),
    path('eventodetail/<int:pk>', EventoDetailView.as_view(), name='eventodetail'),

    path('papeleralist/', PapeleraListView.as_view(), name='papeleralist'),
    path('delete/<str:model_name>/<int:pk>/', DeletePView.as_view(), name='delete'),

    path('categorialist/', CategoriaListView.as_view(), name='categorialist'),
    path('categoricreate/', CategoriaCreateView.as_view(), name='categoriacreate'),
    path('categoriupdate/<int:pk>', CategoriaUpdateView.as_view(), name='categoriaupdate'),
    path('categoriadelete/<int:pk>', CategoriaDeleteView.as_view(), name='categoriadelete'),

    path('partidolist/', PartidoListView.as_view(), name='partidolist'),
    path('partidocreate/', PartidoCreateView.as_view(), name='partidocreate'),
    path('partidoupdate/<int:pk>', PartidoUpdateView.as_view(), name='partidoupdate'),
    path('partidodetail/<int:pk>', PartidoDetailView.as_view(), name='partidodetail'),

    path('logolist/', LogoListView.as_view(), name='logolist'),
    path('logocreate/', LogoCreateView.as_view(), name='logocreate'),
    path('logoupdate/<int:pk>', LogoUpdateView.as_view(), name='logoupdate'),
    path('logodetail/<int:pk>', LogoDetailView.as_view(), name='logodetail'),

    path('fotolist/', FotoDiaListView.as_view(), name='fotolist'),
    path('fotocreate/', FotoDiaCreateView.as_view(), name='fotocreate'),
    path('fotoupdate/<int:pk>', FotoDiaUpdateView.as_view(), name='fotoupdate'),
    path('fotodetail/<int:pk>', FotoDiaDetailView.as_view(), name='fotodetail'),

    path('cartalist/', CartaListView.as_view(), name='cartalist'),
    path('cartacreate/', CartaCreateView.as_view(), name='cartacreate'),
    path('cartaupdate/<int:pk>', CartaUpdateView.as_view(), name='cartaupdate'),
    path('cartadetail/<int:pk>', CartaDetailView.as_view(), name='cartadetail'),

    path('api/', include(router.urls)),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)