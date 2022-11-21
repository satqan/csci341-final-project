from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Record
from .forms import RecordForm
from django.urls import reverse_lazy


class RecordList(ListView):
    template_name = 'list.html'
    model = Record

    def get_context_data(self, **kwargs):
        context = super(RecordList, self).get_context_data(**kwargs)
        context['model_name'] = 'Record'
        return context


class RecordDetail(DetailView):
    template_name = 'detail.html'
    model = Record

    def get_context_data(self, **kwargs):
        context = super(RecordDetail, self).get_context_data(**kwargs)
        context['model_name'] = 'Record'
        return context


class RecordCreate(SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    model = Record
    form_class = RecordForm
    success_url = reverse_lazy('Record_list')
    success_message = "Record successfully created!"

    def get_context_data(self, **kwargs):
        context = super(RecordCreate, self).get_context_data(**kwargs)
        context['model_name'] = 'Record'
        return context


class RecordUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'form.html'
    model = Record
    form_class = RecordForm
    success_url = reverse_lazy('Record_list')
    success_message = "Record successfully updated!"

    def get_context_data(self, **kwargs):
        context = super(RecordUpdate, self).get_context_data(**kwargs)
        context['model_name'] = 'Record'
        return context


class RecordDelete(SuccessMessageMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Record
    success_url = reverse_lazy('Record_list')
    success_message = "Record successfully deleted!"

    def get_context_data(self, **kwargs):
        context = super(RecordDelete, self).get_context_data(**kwargs)
        context['model_name'] = 'Record'
        return context
