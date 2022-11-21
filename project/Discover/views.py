from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Discover
from .forms import DiscoverForm
from django.urls import reverse_lazy


class DiscoverList(ListView):
    template_name = 'list.html'
    model = Discover

    def get_context_data(self, **kwargs):
        context = super(DiscoverList, self).get_context_data(**kwargs)
        context['model_name'] = 'Discover'
        return context


class DiscoverDetail(DetailView):
    template_name = 'detail.html'
    model = Discover

    def get_context_data(self, **kwargs):
        context = super(DiscoverDetail, self).get_context_data(**kwargs)
        context['model_name'] = 'Discover'
        return context


class DiscoverCreate(SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    model = Discover
    form_class = DiscoverForm
    success_url = reverse_lazy('Discover_list')
    success_message = "Discover successfully created!"

    def get_context_data(self, **kwargs):
        context = super(DiscoverCreate, self).get_context_data(**kwargs)
        context['model_name'] = 'Discover'
        return context


class DiscoverUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'form.html'
    model = Discover
    form_class = DiscoverForm
    success_url = reverse_lazy('Discover_list')
    success_message = "Discover successfully updated!"

    def get_context_data(self, **kwargs):
        context = super(DiscoverUpdate, self).get_context_data(**kwargs)
        context['model_name'] = 'Discover'
        return context


class DiscoverDelete(SuccessMessageMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Discover
    success_url = reverse_lazy('Discover_list')
    success_message = "Discover successfully deleted!"

    def get_context_data(self, **kwargs):
        context = super(DiscoverDelete, self).get_context_data(**kwargs)
        context['model_name'] = 'Discover'
        return context

