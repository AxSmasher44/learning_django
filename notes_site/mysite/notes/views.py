from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, Http404
from .models import Note, Topic
from django.db import IntegrityError
from django.utils import timezone

# Create your views here.


def index(request):
    all_topic_list = Topic.objects.all()
    return render(request, 'notes/index.html', {'all_topic_list': all_topic_list})


def view_all_notes(request, topic_slug):

    topic = get_object_or_404(Topic, slug=topic_slug)
    all_notes_list = Note.objects.filter(topic=topic)

    return render(request, 'notes/view.html', {'all_notes_list': all_notes_list, 'topic': topic})


def note(request, note_id):
    note_data = get_object_or_404(Note, pk=note_id)
    return render(request, 'notes/note.html', {'note_data': note_data})


def delete(request, model_type):
    if model_type.upper() == "TOPIC":
        try:
            deleted_section = Topic(pk=request.POST['section_to_be_deleted'])
        except(KeyError, Topic.DoesNotExist):
            pass
        else:
            deleted_section.delete()
        finally:
            return redirect(reverse('notes:index'))
    elif model_type.upper() == "NOTE":
        try:
            deleted_note = Note.objects.get(pk=request.POST['note_to_be_deleted'])

        except(KeyError, Note.DoesNotExist):
            pass
        else:
            deleted_note.delete()
        finally:
            return redirect(reverse('notes:view_all_notes', args=[deleted_note.topic.slug]))


def add(request):
    new_section = Topic(title=request.POST['section_name'])
    new_section.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return redirect(reverse('notes:index'))


def edit(request, sno): # for creating and editing notes

    if request.method == "POST":
        note_topic_id = request.POST['note_topic_id']
        note_topic = Topic.objects.get(pk=note_topic_id)
        title = request.POST['title']
        body = request.POST['body']
        if sno == "0":
            new_note = Note(title=title, body=body, topic=note_topic)
            new_note.save()
            return redirect(reverse('notes:note', args=[new_note.id]))
        else:
            existing_note = Note.objects.get(pk=sno)
            existing_note.title = title
            existing_note.body = body
            existing_note.pub_date = timezone.now()
            existing_note.save()
            return redirect(reverse('notes:note', args=[existing_note.id]))
    # try:
    #     required_note = Note.objects.get(pk=sno)
    #     ctx = {
    #         "note_title": required_note.title,
    #         "note_body": required_note.body,
    #         "note_sno": required_note.id
    #     }
    # except(KeyError, Note.DoesNotExist):
    #     ctx = {
    #         "note_title": "",
    #         "note_body": "",
    #         ""
    #     }
    # finally:
    note_topic_id = request.GET['note_topic_id']
    note_topic = Topic.objects.get(pk=int(note_topic_id))
    try:
        required_note = Note.objects.get(pk=sno)
    except(KeyError, Note.DoesNotExist):
        return render(request, 'notes/edit.html', {"topic_slug":note_topic.slug, "topic_id":note_topic.id})
    else:
        return render(request, 'notes/edit.html', {"required_note":required_note,
                                                   "topic_slug": note_topic.slug,
                                                   "topic_id": note_topic.id})
