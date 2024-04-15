
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets
from .serializers import*
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from cloudinary.uploader import upload

class ArticuloListView(LoginRequiredMixin, ListView):
    model = Articulo  
    template_name = "list.html"
    context_object_name='Articulo'

    def get_queryset(self):
        return Articulo.objects.filter(activo=True)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']='Listado de Artículos'
        return context
    
    def post(self, request, *args, **kwargs):
        selected_ids = request.POST.getlist('seleccionados')
        Articulo.objects.filter(id__in=selected_ids).update(activo=False)
        return HttpResponseRedirect(reverse('articulolist'))

    
class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = "create.html"
    success_url = reverse_lazy('articulolist')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        
        # Guardar el objeto para obtener un ID
        self.object.save()

        # Verificar si se han subido imágenes
        for field in ['foto_1', 'foto_2', 'foto_3', 'foto_4', 'foto_5']:
            imagen = getattr(self.object, field)
            if isinstance(imagen, InMemoryUploadedFile):
                try:
                    # Leer el contenido del archivo desde la memoria
                    image_content = imagen.read()
                    # Subir imagen a Cloudinary
                    result = upload(image_content, public_id=f"{self.object.id}_{field}")
                    setattr(self.object, field, result['secure_url'])
                    
                except Exception as e:
                    # Manejar el error si la imagen no se puede subir a Cloudinary
                    print(f"Error al subir la imagen a Cloudinary: {e}")
                    setattr(self.object, field, None)
        
        self.object.save()
        
        return super().form_valid(form)


class ArticuloUpdateView(LoginRequiredMixin,UpdateView):
    model = Articulo
    form_class= ArticuloForm
    template_name = "edit.html"
    success_url= reverse_lazy('articulolist')

class ArticuloDetailView(LoginRequiredMixin,DetailView):
    model = Articulo
    template_name = "detail.html"
    context_object_name='Articulo'
    success_url= reverse_lazy('articulolist')

class EventoListView(LoginRequiredMixin,ListView):
    model = Evento 
    template_name = "eventolist.html"
    context_object_name='Articulo'

    def get_queryset(self):
        return Evento.objects.filter(activo=True)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']='Listado de Eventos'
        return context
    
    def post(self, request, *args, **kwargs):
        selected_ids = request.POST.getlist('seleccionados')
        Evento.objects.filter(id__in=selected_ids).update(activo=False)
        return HttpResponseRedirect(reverse('eventolist'))
    
class EventoCreateView(LoginRequiredMixin, CreateView):
    model = Evento
    form_class = EventoForm
    template_name = "eventocreate.html"
    success_url = reverse_lazy('eventolist')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        
        # Guardar el objeto para obtener un ID
        self.object.save()

        # Verificar si se han subido imágenes
        for field in ['foto_1', 'foto_2', 'foto_3', 'foto_4', 'foto_5']:
            imagen = getattr(self.object, field)
            if isinstance(imagen, InMemoryUploadedFile):
                try:
                    # Leer el contenido del archivo desde la memoria
                    image_content = imagen.read()
                    # Subir imagen a Cloudinary
                    result = upload(image_content, public_id=f"{self.object.id}_{field}")
                    setattr(self.object, field, result['secure_url'])
                    
                except Exception as e:
                    # Manejar el error si la imagen no se puede subir a Cloudinary
                    print(f"Error al subir la imagen a Cloudinary: {e}")
                    setattr(self.object, field, None)
        
        self.object.save()
        
        return super().form_valid(form)


class EventoUpdateView(LoginRequiredMixin,UpdateView):
    model = Evento
    form_class= EventoForm
    template_name = "eventoedit.html"
    success_url= reverse_lazy('eventolist')

class EventoDetailView(LoginRequiredMixin,DetailView):
    model = Evento
    template_name = "eventodetail.html"
    context_object_name='Articulo'
    success_url= reverse_lazy('eventolist')

class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria  
    template_name = "categorialist.html"
    context_object_name='Articulo'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']='Listado de Categorías'
        return context
       
class CategoriaCreateView(LoginRequiredMixin,CreateView):
    model = Categoria
    form_class= CategoriaForm
    template_name = "categoriacreate.html"
    success_url= reverse_lazy('categorialist')

class CategoriaUpdateView(LoginRequiredMixin,UpdateView):
    model = Categoria
    form_class= CategoriaForm
    template_name = "categoriaedit.html"
    success_url= reverse_lazy('categorialist')

class CategoriaDeleteView(LoginRequiredMixin,DeleteView):
    model = Categoria  
    template_name = 'categoriadelete.html'  
    success_url = reverse_lazy('categorialist')
    context_object_name='object'
    
class PartidoListView(LoginRequiredMixin,ListView):
    model = Partido 
    template_name = "partidolist.html"
    context_object_name='Articulo'

    def get_queryset(self):
        return Partido.objects.filter(activo=True)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']='Deporte en Acción'
        return context
    
    def post(self, request, *args, **kwargs):
        selected_ids = request.POST.getlist('seleccionados')
        Partido.objects.filter(id__in=selected_ids).update(activo=False)
        return HttpResponseRedirect(reverse('partidolist'))
    
class PartidoCreateView(LoginRequiredMixin, CreateView):
    model = Partido
    form_class = PartidoForm
    template_name = "partidocreate.html"
    success_url = reverse_lazy('partidolist')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        
        # Guardar el objeto para obtener un ID
        self.object.save()

        # Verificar si se han subido imágenes
        for field in ['foto_1']:
            imagen = getattr(self.object, field)
            if isinstance(imagen, InMemoryUploadedFile):
                try:
                    # Leer el contenido del archivo desde la memoria
                    image_content = imagen.read()
                    # Subir imagen a Cloudinary
                    result = upload(image_content, public_id=f"{self.object.id}_{field}")
                    setattr(self.object, field, result['secure_url'])
                    
                except Exception as e:
                    # Manejar el error si la imagen no se puede subir a Cloudinary
                    print(f"Error al subir la imagen a Cloudinary: {e}")
                    setattr(self.object, field, None)
        
        self.object.save()
        
        return super().form_valid(form)


class PartidoUpdateView(LoginRequiredMixin,UpdateView):
    model = Partido
    form_class= PartidoForm
    template_name = "partidoedit.html"
    success_url= reverse_lazy('partidolist')

class PartidoDetailView(LoginRequiredMixin,DetailView):
    model = Partido
    template_name = "partidodetail.html"
    context_object_name='Articulo'
    success_url= reverse_lazy('partidolist')

class LogoListView(LoginRequiredMixin,ListView):
    model = Logo
    template_name = "logolist.html"
    context_object_name='Articulo'

    def get_queryset(self):
        return Logo.objects.filter(activo=True)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']='Logo'
        return context
    
    def post(self, request, *args, **kwargs):
        selected_ids = request.POST.getlist('seleccionados')
        Logo.objects.filter(id__in=selected_ids).update(activo=False)
        return HttpResponseRedirect(reverse('logolist'))
    
class LogoCreateView(LoginRequiredMixin, CreateView):
    model = Logo
    form_class = LogoForm
    template_name = "logocreate.html"
    success_url = reverse_lazy('logolist')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        
        # Guardar el objeto para obtener un ID
        self.object.save()

        # Verificar si se han subido imágenes
        for field in ['foto_1']:
            imagen = getattr(self.object, field)
            if isinstance(imagen, InMemoryUploadedFile):
                try:
                    # Leer el contenido del archivo desde la memoria
                    image_content = imagen.read()
                    # Subir imagen a Cloudinary
                    result = upload(image_content, public_id=f"{self.object.id}_{field}")
                    setattr(self.object, field, result['secure_url'])
                    
                except Exception as e:
                    # Manejar el error si la imagen no se puede subir a Cloudinary
                    print(f"Error al subir la imagen a Cloudinary: {e}")
                    setattr(self.object, field, None)
        
        self.object.save()
        
        return super().form_valid(form)


class LogoUpdateView(LoginRequiredMixin,UpdateView):
    model = Logo
    form_class= LogoForm
    template_name = "logoedit.html"
    success_url= reverse_lazy('logolist')

class LogoDetailView(LoginRequiredMixin,DetailView):
    model = Logo
    template_name = "logodetail.html"
    context_object_name='Articulo'
    success_url= reverse_lazy('logolist')

class FotoDiaListView(LoginRequiredMixin,ListView):
    model = Foto_Día
    template_name = "fotolist.html"
    context_object_name='Articulo'

    def get_queryset(self):
        return Foto_Día.objects.filter(activo=True)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']='Foto del Día'
        return context
    
    def post(self, request, *args, **kwargs):
        selected_ids = request.POST.getlist('seleccionados')
        Foto_Día.objects.filter(id__in=selected_ids).update(activo=False)
        return HttpResponseRedirect(reverse('fotolist'))
    
class FotoDiaCreateView(LoginRequiredMixin, CreateView):
    model = Foto_Día
    form_class = Foto_DíaForm
    template_name = "fotocreate.html"
    success_url = reverse_lazy('fotolist')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        
        # Guardar el objeto para obtener un ID
        self.object.save()

        # Verificar si se han subido imágenes
        for field in ['foto_1']:
            imagen = getattr(self.object, field)
            if isinstance(imagen, InMemoryUploadedFile):
                try:
                    # Leer el contenido del archivo desde la memoria
                    image_content = imagen.read()
                    # Subir imagen a Cloudinary
                    result = upload(image_content, public_id=f"{self.object.id}_{field}")
                    setattr(self.object, field, result['secure_url'])
                    
                except Exception as e:
                    # Manejar el error si la imagen no se puede subir a Cloudinary
                    print(f"Error al subir la imagen a Cloudinary: {e}")
                    setattr(self.object, field, None)
        
        self.object.save()
        
        return super().form_valid(form)


class FotoDiaUpdateView(LoginRequiredMixin,UpdateView):
    model = Foto_Día
    form_class= Foto_DíaForm
    template_name = "fotoedit.html"
    success_url= reverse_lazy('fotolist')

class FotoDiaDetailView(LoginRequiredMixin,DetailView):
    model = Foto_Día
    template_name = "fotodetail.html"
    context_object_name='Articulo'
    success_url= reverse_lazy('fotolist')

class CartaListView(LoginRequiredMixin,ListView):
    model = Carta
    template_name = "cartalist.html"
    context_object_name='Articulo'

    def get_queryset(self):
        return Carta.objects.filter(activo=True)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']='Cartas al Editor'
        return context
    
    def post(self, request, *args, **kwargs):
        selected_ids = request.POST.getlist('seleccionados')
        Carta.objects.filter(id__in=selected_ids).update(activo=False)
        return HttpResponseRedirect(reverse('cartalist'))

class CartaCreateView(LoginRequiredMixin, CreateView):
    model = Carta
    form_class = CartaForm
    template_name = "cartacreate.html"
    success_url = reverse_lazy('cartalist')

class CartaUpdateView(LoginRequiredMixin,UpdateView):
    model = Carta
    form_class= CartaForm
    template_name = "cartaedit.html"
    success_url= reverse_lazy('cartalist')

class CartaDetailView(LoginRequiredMixin,DetailView):
    model = Carta
    template_name = "cartadetail.html"
    context_object_name='Articulo'
    success_url= reverse_lazy('cartalist')

class PapeleraListView(LoginRequiredMixin, ListView):
    model = Articulo  
    template_name = "papelera.html"
    context_object_name='Articulo'

    def get_queryset(self):
        return Articulo.objects.filter(activo=False)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']='Papelera '
        context['Evento'] = Evento.objects.filter(activo=False)
        context['Foto'] = Foto_Día.objects.filter(activo=False)
        context['Logo'] = Logo.objects.filter(activo=False)
        context['Partido'] = Partido.objects.filter(activo=False)
        context['Carta'] = Carta.objects.filter(activo=False)
        return context
    
    def post(self, request, *args, **kwargs):
        if 'activar_articulo' in request.POST:
            selected_ids = request.POST.getlist('seleccionados_articulo', [])
            Articulo.objects.filter(id__in=selected_ids).update(activo=True)
        elif 'activar_evento' in request.POST:
            selected_ids = request.POST.getlist('seleccionados_evento', [])
            Evento.objects.filter(id__in=selected_ids).update(activo=True)
        elif 'activar_foto' in request.POST:
            selected_ids = request.POST.getlist('seleccionados_foto', [])
            Foto_Día.objects.filter(id__in=selected_ids).update(activo=True)
        elif 'activar_logo' in request.POST:
            selected_ids = request.POST.getlist('seleccionados_logo', [])
            Logo.objects.filter(id__in=selected_ids).update(activo=True)
        elif 'activar_partido' in request.POST:
            selected_ids = request.POST.getlist('seleccionados_partido', [])
            Partido.objects.filter(id__in=selected_ids).update(activo=True)
        elif 'activar_carta' in request.POST:
            selected_ids = request.POST.getlist('seleccionados_carta', [])
            Carta.objects.filter(id__in=selected_ids).update(activo=True)
        
        return HttpResponseRedirect(reverse('papeleralist'))
    
class DeletePView(LoginRequiredMixin, DeleteView):
    model = None  
    template_name = 'delete.html'  
    success_url = reverse_lazy('papeleralist')

    def get_object(self, queryset=None):

        model_name = self.kwargs.get('model_name', None)
        if model_name == 'articulo':
            self.model = Articulo
        elif model_name == 'evento':
            self.model = Evento
        elif model_name == 'foto':
            self.model = Foto_Día
        elif model_name == 'logo':
            self.model = Logo
        elif model_name == 'partido':
            self.model = Partido
        elif model_name == 'carta':
            self.model = Carta
        return super().get_object(queryset)

    def get_success_url(self):
        if self.model == Articulo:
            return reverse_lazy('papeleralist')
        elif self.model == Evento:
            return reverse_lazy('papeleralist')
        elif self.model == Foto_Día:
            return reverse_lazy('papeleralist')
        elif self.model == Logo:
            return reverse_lazy('papeleralist')
        elif self.model == Partido:
            return reverse_lazy('papeleralist')
        elif self.model == Carta:
            return reverse_lazy('papeleralist')
        
class ArticuloViewSet(viewsets.ModelViewSet):  
    serializer_class = ArticuloSerializer
    
    def get_queryset(self):
        queryset = Articulo.objects.filter(activo=True, publicado=True)
        categoria = self.request.query_params.get('categoria', None)

        if categoria is not None:
            queryset = queryset.filter(categoria=categoria)

        return queryset

class ArticuloIndividualViewSet(viewsets.ModelViewSet):  
    serializer_class = ArticuloSerializer
    
    def get_queryset(self):
        queryset = Articulo.objects.filter(activo=True, publicado=True)
        articulo_id = self.request.query_params.get('id', None)

        if articulo_id is not None:
            queryset = queryset.filter(id=articulo_id)

        return queryset

class EventoViewSet(viewsets.ModelViewSet): 
    serializer_class = EventoSerializer

    def get_queryset(self):
        queryset = Evento.objects.filter(activo=True, publicado=True)
        categoria = self.request.query_params.get('categoria', None)

        if categoria is not None:
            queryset = queryset.filter(categoria=categoria)

        return queryset
    
class PartidoViewSet(viewsets.ModelViewSet): 
    serializer_class = PartidoSerializer

    def get_queryset(self):
        queryset = Partido.objects.filter(activo=True, publicado=True)
        return queryset
    
class FotoDiaViewSet(viewsets.ModelViewSet): 
    serializer_class = FotoDiaSerializer

    def get_queryset(self):
        queryset = Foto_Día.objects.filter(activo=True, publicado=True)
        return queryset
    
class LogoViewSet(viewsets.ModelViewSet): 
    serializer_class = LogoSerializer

    def get_queryset(self):
        queryset = Logo.objects.filter(activo=True, publicado=True)
        return queryset
    
class CartaViewSet(viewsets.ModelViewSet): 
    serializer_class = CartaSerializer

    def get_queryset(self):
        queryset = Carta.objects.filter(activo=True, publicado=True)
        return queryset