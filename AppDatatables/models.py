from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=255, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = ("Categoría")
        verbose_name_plural = ("Categorías")
        ordering = ['id']

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    autor=models.CharField(max_length=255, blank=True, null=True)
    titulo=models.CharField(max_length=255, blank=True, null=True)
    introduccion=models.TextField(blank=True, null=True)
    foto_1=CloudinaryField('image', blank=True, null=True)
    foto_2=CloudinaryField('image', blank=True, null=True)
    foto_3=CloudinaryField('image', blank=True, null=True)
    foto_4=CloudinaryField('image', blank=True, null=True)
    foto_5=CloudinaryField('image', blank=True, null=True)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion=models.TextField(blank=True, null=True)
    descripcion2=models.TextField(blank=True, null=True)
    descripcion3=models.TextField(blank=True, null=True)
    descripcion4=models.TextField(blank=True, null=True)
    descripcion5=models.TextField(blank=True, null=True)
    no_edicion=models.IntegerField(default=0,blank=True, null=True)
    activo=models.BooleanField(default=1, blank=True, null=True)
    fecha_de_registro=models.DateTimeField(auto_now_add=True)
    publicado=models.BooleanField(default=0)

    class Meta:
        verbose_name = ("Artículo")
        verbose_name_plural = ("Artículos")
        ordering = ['id']

    def __str__(self):
        return self.titulo
    
class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=255, blank=True, null=True)
    descripcion=models.TextField(blank=True, null=True)
    descripcion2=models.TextField(blank=True, null=True)
    descripcion3=models.TextField(blank=True, null=True)
    descripcion4=models.TextField(blank=True, null=True)
    descripcion5=models.TextField(blank=True, null=True)
    fecha_de_evento=models.DateField(blank=True, null=True)
    hora_inicio=models.TimeField(blank=True, null=True)
    hora_final=models.TimeField(blank=True, null=True)
    lugar=models.CharField(max_length=255, blank=True, null=True)
    foto_1=CloudinaryField('image', blank=True, null=True)
    foto_2=CloudinaryField('image', blank=True, null=True)
    foto_3=CloudinaryField('image', blank=True, null=True)
    foto_4=CloudinaryField('image', blank=True, null=True)
    foto_5=CloudinaryField('image', blank=True, null=True)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    activo=models.BooleanField(default=1)
    fecha_de_registro=models.DateTimeField(auto_now_add=True)
    publicado=models.BooleanField(default=0)

    class Meta:
        verbose_name = ("Evento")
        verbose_name_plural = ("Eventos")
        ordering = ['id']

    def __str__(self):
        return self.nombre
    
class Partido(models.Model):
    id = models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=255, blank=True, null=True)
    descripcion=models.TextField(blank=True, null=True)
    descripcion2=models.TextField(blank=True, null=True)
    descripcion3=models.TextField(blank=True, null=True)
    descripcion4=models.TextField(blank=True, null=True)
    descripcion5=models.TextField(blank=True, null=True)
    recomendacion=models.TextField(blank=True, null=True)
    fecha_de_evento=models.DateField(blank=True, null=True)
    hora_inicio=models.TimeField(blank=True, null=True)
    lugar=models.CharField(max_length=255, blank=True, null=True)
    foto_1=CloudinaryField('image', blank=True, null=True)
    foto_2=CloudinaryField('image', blank=True, null=True)
    foto_3=CloudinaryField('image', blank=True, null=True)
    foto_4=CloudinaryField('image', blank=True, null=True)
    foto_5=CloudinaryField('image', blank=True, null=True)
    activo=models.BooleanField(default=1)
    fecha_de_registro=models.DateTimeField(auto_now_add=True)
    publicado=models.BooleanField(default=0)

    class Meta:
        verbose_name = ("Partido")
        verbose_name_plural = ("Partidos")
        ordering = ['id']

    def __str__(self):
        return self.titulo

class Foto_Día(models.Model):
    id = models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=255, blank=True, null=True)
    foto_1=CloudinaryField('image', blank=True, null=True)
    activo=models.BooleanField(default=1)
    fecha_de_registro=models.DateTimeField(auto_now_add=True)
    publicado=models.BooleanField(default=1)

    class Meta:
        verbose_name = ("Foto del día")
        verbose_name_plural = ("Foto del día")
        ordering = ['id']

    def __str__(self):
        return self.titulo
    
class Logo(models.Model):
    id = models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=255, blank=True, null=True)
    foto_1=CloudinaryField('image', blank=True, null=True)
    activo=models.BooleanField(default=1)
    fecha_de_registro=models.DateTimeField(auto_now_add=True)
    publicado=models.BooleanField(default=1)

    class Meta:
        verbose_name = ("Logo")
        verbose_name_plural = ("Logo")
        ordering = ['id']

    def __str__(self):
        return self.titulo

class Carta(models.Model):
    id = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=255, blank=True, null=True)
    asunto=models.CharField(max_length=255, blank=True, null=True)
    descripcion=models.TextField(blank=True, null=True)
    activo=models.BooleanField(default=1, blank=True, null=True)
    fecha_de_registro=models.DateTimeField(auto_now_add=True)
    publicado=models.BooleanField(default=0)

    class Meta:
        verbose_name = ("Carta")
        verbose_name_plural = ("Cartas")
        ordering = ['id']

    def __str__(self):
        return self.asunto