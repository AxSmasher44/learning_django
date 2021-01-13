from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hey, sup bruh!</h1>")