from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Doctor
from .forms import DoctorForm
from django.urls import reverse_lazy


class DoctorList(ListView):
    template_name = 'list.html'
    model = Doctor

    def get_context_data(self, **kwargs):
        context = super(DoctorList, self).get_context_data(**kwargs)
        context['model_name'] = 'Doctor'
        return context


class DoctorDetail(DetailView):
    template_name = 'detail.html'
    model = Doctor

    def get_context_data(self, **kwargs):
        context = super(DoctorDetail, self).get_context_data(**kwargs)
        context['model_name'] = 'Doctor'
        return context


class DoctorCreate(SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy('Doctor_list')
    success_message = "Doctor successfully created!"

    def get_context_data(self, **kwargs):
        context = super(DoctorCreate, self).get_context_data(**kwargs)
        context['model_name'] = 'Doctor'
        return context


class DoctorUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'form.html'
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy('Doctor_list')
    success_message = "Doctor successfully updated!"

    def get_context_data(self, **kwargs):
        context = super(DoctorUpdate, self).get_context_data(**kwargs)
        context['model_name'] = 'Doctor'
        return context


class DoctorDelete(SuccessMessageMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Doctor
    success_url = reverse_lazy('Doctor_list')
    success_message = "Doctor successfully deleted!"

    def get_context_data(self, **kwargs):
        context = super(DoctorDelete, self).get_context_data(**kwargs)
        context['model_name'] = 'Doctor'
        return context
