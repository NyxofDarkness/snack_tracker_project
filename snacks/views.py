from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from snacks.models import Snack

class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack

class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack

class SnackCreateView(CreateView):
    template_name = 'snack_create.html'
    model = Snack

class SnackUpdateView(UpdateView):
    template_name = 'snack_update.html'
    model = Snack

class SnackDeleteView(DeleteView):
    template_name = 'snack_delete.html'
    model = Snack
