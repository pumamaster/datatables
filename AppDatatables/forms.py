from django import forms
from .models import *

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo  
        fields = ['autor', 'titulo', 'descripcion', 'introduccion',
                  'foto_1',
                  'foto_2',
                  'foto_3',
                  'foto_4',
                  'foto_5',
                  'categoria','descripcion','descripcion2','descripcion3','descripcion4','descripcion5','no_edicion', 'publicado']  
        
    def __init__(self, *args, **kwargs):
        super(ArticuloForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['foto_1'].widget.attrs.update({})
        self.fields['foto_2'].widget.attrs.update({})
        self.fields['foto_3'].widget.attrs.update({})
        self.fields['foto_4'].widget.attrs.update({})
        self.fields['foto_5'].widget.attrs.update({})

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento  
        fields = ['nombre', 'descripcion','descripcion2','descripcion3','descripcion4','descripcion5', 'fecha_de_evento', 'lugar',
                  'foto_1',
                  'foto_2',
                  'foto_3',
                  'foto_4',
                  'foto_5',
                  'categoria','publicado','hora_inicio','hora_final']  
        
    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['foto_1'].widget.attrs.update({})
        self.fields['foto_2'].widget.attrs.update({})
        self.fields['foto_3'].widget.attrs.update({})
        self.fields['foto_4'].widget.attrs.update({})
        self.fields['foto_5'].widget.attrs.update({})


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria 
        fields = ['nombre']  

class LogoForm(forms.ModelForm):
    class Meta:
        model = Logo 
        fields = ['titulo',
                  'foto_1',]  
    def __init__(self, *args, **kwargs):
        super(LogoForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['foto_1'].widget.attrs.update({})

class Foto_DíaForm(forms.ModelForm):
    class Meta:
        model = Foto_Día
        fields = ['titulo',
                  'foto_1',]  
        def __init__(self, *args, **kwargs):
            super(Foto_DíaForm, self).__init__(*args, **kwargs)
            for field_name in self.fields:
                self.fields[field_name].widget.attrs.update({
                    'class': 'form-control'
                })
            self.fields['foto_1'].widget.attrs.update({})

class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = ['titulo', 'descripcion','descripcion2','descripcion3','descripcion4','descripcion5', 'recomendacion', 'lugar',
                  'foto_1',
                  'foto_2',
                  'foto_3',
                  'foto_4',
                  'foto_5',
                  'publicado','hora_inicio','fecha_de_evento']   
        
        def __init__(self, *args, **kwargs):
            super(PartidoForm, self).__init__(*args, **kwargs)
            for field_name in self.fields:
                self.fields[field_name].widget.attrs.update({
                    'class': 'form-control'
                })
            self.fields['foto_1'].widget.attrs.update({})
            self.fields['foto_2'].widget.attrs.update({})
            self.fields['foto_3'].widget.attrs.update({})
            self.fields['foto_4'].widget.attrs.update({})
            self.fields['foto_5'].widget.attrs.update({})

class CartaForm(forms.ModelForm):
    class Meta:
        model = Carta
        fields = ['nombre', 'descripcion', 'asunto',
                  'publicado',]  
        
        def __init__(self, *args, **kwargs):
            super(PartidoForm, self).__init__(*args, **kwargs)
            for field_name in self.fields:
                self.fields[field_name].widget.attrs.update({
                    'class': 'form-control'
                })
