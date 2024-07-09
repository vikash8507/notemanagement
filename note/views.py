from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from note.models import Note
from note.forms import NoteForm
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

class NoteListView(ListView):
    model = Note
    context_object_name = "notes"
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Note]:
        return super().get_queryset().filter(author=self.request.user)

class NoteDetailView(DetailView):
    model = Note


class NoteCreateView(SuccessMessageMixin, CreateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy("note:note_list")
    success_message = "Note Created Successfully!"


    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            form.instance.author = request.user
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class NoteUpdateView(SuccessMessageMixin, UpdateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy("note:note_list")
    success_message = "Note Updated Successfully!"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object and self.object.author != request.user:
            raise PermissionDenied()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object and self.object.author != request.user:
            raise PermissionDenied()
        return super().post(request, *args, **kwargs)



class NoteDeleteView(SuccessMessageMixin, DeleteView):
    model = Note
    success_url = reverse_lazy("note:note_list")
    success_message = "Note Deleted Successfully!"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object and self.object.author != request.user:
            raise PermissionDenied()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object and self.object.author != request.user:
            raise PermissionDenied()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
