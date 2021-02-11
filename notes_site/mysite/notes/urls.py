from django.urls import path
from . import views


app_name = 'notes'
urlpatterns = [
    path('sections/', views.index, name='index'),
    path('all_notes/<slug:topic_slug>/', views.view_all_notes, name='view_all_notes'),
    path('view/<int:note_id>/', views.note, name='note'),
    path('delete/<str:model_type>', views.delete, name='delete'),
    path('add/', views.add, name="add_section"),
    path("edit/<str:sno>/", views.edit, name="edit")
]
# try:
#     required_note = Note.objects.get(pk=sno)
# except(KeyError, Note.DoesNotExist):
#     raise Http404("Page not found")
# else:
#     return render(request, 'notes/edit.html', {"required_note":required_note,
#                                                "topic_slug":required_note.topic.slug,
#                                                "topic_id": required_note.topic.id})
