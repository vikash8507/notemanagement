#-*- coding:utf-8 -*-

from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from note import views

# namespace
app_name = 'note'

urlpatterns = [
    # Fetch note list
    path('', login_required(views.NoteListView.as_view(), login_url="/login/"), name='note_list'),
    # Create a note
    path('create/',login_required( views.NoteCreateView.as_view(), login_url="/login/"), name='note_create'),
    # Update a note
    re_path(r'^(?P<pk>\d+)/detail/$', login_required(views.NoteDetailView.as_view(), login_url="/login/"), name='note_detail'),
    # Detail of a note
    re_path(r'^(?P<pk>\d+)/update/$', login_required(views.NoteUpdateView.as_view(), login_url="/login/"), name='note_update'),
    # Delete a note
    re_path(r'^(?P<pk>\d+)/delete/$', login_required(views.NoteDeleteView.as_view(), login_url="/login/"), name='note_delete')

]
