from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import Notes
from .forms import NotesForm

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/notes'
    template_name = 'notes/notes_delete.html'
    login_url = "/login"

class NotesUpdateView(UpdateView):
    model = Notes
    #fields = ['title', 'text']
    success_url='/notes'
    form_class = NotesForm
    login_url = "/login"

class NotesCreateView(CreateView):
    model = Notes
    #fields = ['title', 'text']
    success_url='/notes'
    form_class = NotesForm
    login_url = "/login"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
 

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    login_url = "/login"
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