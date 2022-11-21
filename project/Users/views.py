from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Users
from .forms import UsersForm
from django.urls import reverse_lazy


class UsersList(ListView):
    template_name = 'list.html'
    model = Users

    def get_context_data(self, **kwargs):
        context = super(UsersList, self).get_context_data(**kwargs)
        context['model_name'] = 'Users'
        return context


class UsersDetail(DetailView):
    template_name = 'detail.html'
    model = Users

    def get_context_data(self, **kwargs):
        context = super(UsersDetail, self).get_context_data(**kwargs)
        context['model_name'] = 'Users'
        return context


class UsersCreate(SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    model = Users
    form_class = UsersForm
    success_url = reverse_lazy('Users_list')
    success_message = "Users successfully created!"

    def get_context_data(self, **kwargs):
        context = super(UsersCreate, self).get_context_data(**kwargs)
        context['model_name'] = 'Users'
        return context


class UsersUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'form.html'
    model = Users
    form_class = UsersForm
    success_url = reverse_lazy('Users_list')
    success_message = "Users successfully updated!"

    def get_context_data(self, **kwargs):
        context = super(UsersUpdate, self).get_context_data(**kwargs)
        context['model_name'] = 'Users'
        return context


class UsersDelete(SuccessMessageMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Users
    success_url = reverse_lazy('Users_list')
    success_message = "Users successfully deleted!"

    def get_context_data(self, **kwargs):
        context = super(UsersDelete, self).get_context_data(**kwargs)
        context['model_name'] = 'Users'
        return context
