from django.shortcuts import render
from django.http import HttpResponse
from .models import Note, Topic


# Create your views here.
def index(request):
    all_topic_list = Topic.objects.all()
    return render(request, 'notes/index.html', {'all_topic_list': all_topic_list})


def view_notes(request, topic_slug):
    topic = Topic.objects.get(slug=topic_slug)
    all_notes_list = Note.objects.filter(topic=topic)
    return render(request, 'notes/view.html', {'all_notes_list': all_notes_list, 'topic': topic.title})
