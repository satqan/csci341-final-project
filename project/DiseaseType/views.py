from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import DiseaseType
from .forms import DiseaseTypeForm
from django.urls import reverse_lazy


class DiseaseTypeList(ListView):
    template_name = 'list.html'
    model = DiseaseType

    def get_context_data(self, **kwargs):
        context = super(DiseaseTypeList, self).get_context_data(**kwargs)
        context['model_name'] = 'DiseaseType'
        return context


class DiseaseTypeDetail(DetailView):
    template_name = 'detail.html'
    model = DiseaseType

    def get_context_data(self, **kwargs):
        context = super(DiseaseTypeDetail, self).get_context_data(**kwargs)
        context['model_name'] = 'DiseaseType'
        return context


class DiseaseTypeCreate(SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    model = DiseaseType
    form_class = DiseaseTypeForm
    success_url = reverse_lazy('DiseaseType_list')
    success_message = "DiseaseType successfully created!"

    def get_context_data(self, **kwargs):
        context = super(DiseaseTypeCreate, self).get_context_data(**kwargs)
        context['model_name'] = 'DiseaseType'
        return context


class DiseaseTypeUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'form.html'
    model = DiseaseType
    form_class = DiseaseTypeForm
    success_url = reverse_lazy('DiseaseType_list')
    success_message = "DiseaseType successfully updated!"

    def get_context_data(self, **kwargs):
        context = super(DiseaseTypeUpdate, self).get_context_data(**kwargs)
        context['model_name'] = 'DiseaseType'
        return context


class DiseaseTypeDelete(SuccessMessageMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = DiseaseType
    success_url = reverse_lazy('DiseaseType_list')
    success_message = "DiseaseType successfully deleted!"

    def get_context_data(self, **kwargs):
        context = super(DiseaseTypeDelete, self).get_context_data(**kwargs)
        context['model_name'] = 'DiseaseType'
        return context
