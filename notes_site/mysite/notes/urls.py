from django.urls import path
from . import views


app_name = 'notes'
urlpatterns = [
    path('sections/', views.index, name='index'),
    path('sub_sections/<slug:topic_slug>/', views.view_notes, name='view_notes'),
    path('view/<int:note_id>/', views.note, name='note')

]
