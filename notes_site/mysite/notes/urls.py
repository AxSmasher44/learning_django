from django.urls import path
from . import views


app_name = 'notes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:topic_slug>/', views.view_notes, name='view_notes')
]
