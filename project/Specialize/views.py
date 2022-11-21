from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Specialize
from .forms import SpecializeForm
from django.urls import reverse_lazy


class SpecializeList(ListView):
    template_name = 'list.html'
    model = Specialize

    def get_context_data(self, **kwargs):
        context = super(SpecializeList, self).get_context_data(**kwargs)
        context['model_name'] = 'Specialize'
        return context


class SpecializeDetail(DetailView):
    template_name = 'detail.html'
    model = Specialize

    def get_context_data(self, **kwargs):
        context = super(SpecializeDetail, self).get_context_data(**kwargs)
        context['model_name'] = 'Specialize'
        return context


class SpecializeCreate(SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    model = Specialize
    form_class = SpecializeForm
    success_url = reverse_lazy('Specialize_list')
    success_message = "Specialize successfully created!"

    def get_context_data(self, **kwargs):
        context = super(SpecializeCreate, self).get_context_data(**kwargs)
        context['model_name'] = 'Specialize'
        return context


class SpecializeUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'form.html'
    model = Specialize
    form_class = SpecializeForm
    success_url = reverse_lazy('Specialize_list')
    success_message = "Specialize successfully updated!"

    def get_context_data(self, **kwargs):
        context = super(SpecializeUpdate, self).get_context_data(**kwargs)
        context['model_name'] = 'Specialize'
        return context


class SpecializeDelete(SuccessMessageMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Specialize
    success_url = reverse_lazy('Specialize_list')
    success_message = "Specialize successfully deleted!"

    def get_context_data(self, **kwargs):
        context = super(SpecializeDelete, self).get_context_data(**kwargs)
        context['model_name'] = 'Specialize'
        return context
