from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import PublicServant
from .forms import PublicServantForm
from django.urls import reverse_lazy


class PublicServantList(ListView):
    template_name = 'list.html'
    model = PublicServant

    def get_context_data(self, **kwargs):
        context = super(PublicServantList, self).get_context_data(**kwargs)
        context['model_name'] = 'PublicServant'
        return context


class PublicServantDetail(DetailView):
    template_name = 'detail.html'
    model = PublicServant

    def get_context_data(self, **kwargs):
        context = super(PublicServantDetail, self).get_context_data(**kwargs)
        context['model_name'] = 'PublicServant'
        return context


class PublicServantCreate(SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    model = PublicServant
    form_class = PublicServantForm
    success_url = reverse_lazy('PublicServant_list')
    success_message = "PublicServant successfully created!"

    def get_context_data(self, **kwargs):
        context = super(PublicServantCreate, self).get_context_data(**kwargs)
        context['model_name'] = 'PublicServant'
        return context


class PublicServantUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'form.html'
    model = PublicServant
    form_class = PublicServantForm
    success_url = reverse_lazy('PublicServant_list')
    success_message = "PublicServant successfully updated!"

    def get_context_data(self, **kwargs):
        context = super(PublicServantUpdate, self).get_context_data(**kwargs)
        context['model_name'] = 'PublicServant'
        return context


class PublicServantDelete(SuccessMessageMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = PublicServant
    success_url = reverse_lazy('PublicServant_list')
    success_message = "PublicServant successfully deleted!"

    def get_context_data(self, **kwargs):
        context = super(PublicServantDelete, self).get_context_data(**kwargs)
        context['model_name'] = 'PublicServant'
        return context
