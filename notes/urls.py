
from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotesListView.as_view(), name="notes.list"),
    path('new', views.NotesCreateView.as_view(), name="notes.new"),
    path('<int:pk>/edit', views.NotesUpdateView.as_view(), name="notes.update"),
    path('<int:pk>/delete', views.NotesDeleteView.as_view(), name="notes.delete"),
    #path('<int:pk>', views.detail),
    path('<int:pk>', views.NotesDetailView.as_view(), name="notes.detail")
]
