from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.
from .models import Notes

class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'text']
    success_url='/notes'

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    # template_name = "notes/notes_detail.html"  

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Notes doesn't exist!!!")
#     return render(request, 'notes/notes_detail.html', {'note': note})