from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Country
from .forms import CountryForm
from django.urls import reverse_lazy


class CountryList(ListView):
    template_name = 'list.html'
    model = Country

    def get_context_data(self, **kwargs):
        context = super(CountryList, self).get_context_data(**kwargs)
        context['model_name'] = 'Country'
        return context


class CountryDetail(DetailView):
    template_name = 'detail.html'
    model = Country

    def get_context_data(self, **kwargs):
        context = super(CountryDetail, self).get_context_data(**kwargs)
        context['model_name'] = 'Country'
        return context


class CountryCreate(SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    model = Country
    form_class = CountryForm
    success_url = reverse_lazy('Country_list')
    success_message = "Country successfully created!"

    def get_context_data(self, **kwargs):
        context = super(CountryCreate, self).get_context_data(**kwargs)
        context['model_name'] = 'Country'
        return context


class CountryUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'form.html'
    model = Country
    form_class = CountryForm
    success_url = reverse_lazy('Country_list')
    success_message = "Country successfully updated!"

    def get_context_data(self, **kwargs):
        context = super(CountryUpdate, self).get_context_data(**kwargs)
        context['model_name'] = 'Country'
        return context


class CountryDelete(SuccessMessageMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Country
    success_url = reverse_lazy('Country_list')
    success_message = "Country successfully deleted!"

    def get_context_data(self, **kwargs):
        context = super(CountryDelete, self).get_context_data(**kwargs)
        context['model_name'] = 'Country'
        return context
