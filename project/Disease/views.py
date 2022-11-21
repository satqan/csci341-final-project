from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Disease
from .forms import DiseaseForm
from django.urls import reverse_lazy


class DiseaseList(ListView):
    template_name = 'list.html'
    model = Disease

    def get_context_data(self, **kwargs):
        context = super(DiseaseList, self).get_context_data(**kwargs)
        context['model_name'] = 'Disease'
        return context


class DiseaseDetail(DetailView):
    template_name = 'detail.html'
    model = Disease

    def get_context_data(self, **kwargs):
        context = super(DiseaseDetail, self).get_context_data(**kwargs)
        context['model_name'] = 'Disease'
        return context


class DiseaseCreate(SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    model = Disease
    form_class = DiseaseForm
    success_url = reverse_lazy('Disease_list')
    success_message = "Disease successfully created!"

    def get_context_data(self, **kwargs):
        context = super(DiseaseCreate, self).get_context_data(**kwargs)
        context['model_name'] = 'Disease'
        return context


class DiseaseUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'form.html'
    model = Disease
    form_class = DiseaseForm
    success_url = reverse_lazy('Disease_list')
    success_message = "Disease successfully updated!"

    def get_context_data(self, **kwargs):
        context = super(DiseaseUpdate, self).get_context_data(**kwargs)
        context['model_name'] = 'Disease'
        return context


class DiseaseDelete(SuccessMessageMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Disease
    success_url = reverse_lazy('Disease_list')
    success_message = "Disease successfully deleted!"

    def get_context_data(self, **kwargs):
        context = super(DiseaseDelete, self).get_context_data(**kwargs)
        context['model_name'] = 'Disease'
        return context
