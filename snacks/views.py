from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack

class SnackListView(ListView):
    snack_list = 'snack_list.html'
    model = Snack

class SnackDetailView(DetailView):
    snack_detail = 'snack_detail.html'
    model = Snack

class SnackCreateView(CreateView):
    snack_create = 'snack_create.html'
    model = Snack

class SnackUpdateView(UpdateView):
    snack_update = 'snack_update.html'
    model = Snack

class SnackDeleteView(DeleteView):
    snack_delete = 'snack_delete.html'
    model = Snack
