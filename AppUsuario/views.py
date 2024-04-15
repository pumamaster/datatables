from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from django.views import View
from .forms import LoginForm, RegistroForm, UsuarioUpdateForm, UsuarioPasswordForm
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView

from django.views.generic import ListView, TemplateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from .models import Usuario
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('articulolist')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)
        
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        
        if user is not None:
            
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            form.add_error(None, "Invalid username or password.")
            return self.form_invalid(form)

class LogoutView(LoginRequiredMixin,View):
    def get(self, request):
        logout(request)
        return redirect('loginview')
    
class RegistrarView(LoginRequiredMixin,FormView):
    template_name = 'registro.html'
    form_class = RegistroForm
    success_url = reverse_lazy('usuariolist')

    def form_valid(self, form):
        usuario = form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class ListaUsuarioView(LoginRequiredMixin,ListView):
    model = Usuario 
    template_name = "usuariolist.html"
    context_object_name='Articulo'

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']='Listado de Usuarios'
        return context
    
class UsuarioUpdateView(LoginRequiredMixin,UpdateView):
    model = Usuario
    form_class = UsuarioUpdateForm
    template_name = 'usuarioedit.html'
    success_url = reverse_lazy('usuariolist')

    def get_object(self, queryset=None):
        return self.request.user  

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs

    def form_valid(self, form):
        password = form.cleaned_data['password']
        if password:
            form.instance.set_password(password)
            form.instance.save()  
            logout(self.request)  
            return redirect('loginview') 
        return super().form_valid(form)
    
class UsuarioDeleteView(LoginRequiredMixin,DeleteView):
    model = Usuario  
    template_name = 'usuariodelete.html'  
    success_url = reverse_lazy('usuariolist')
    context_object_name='object'