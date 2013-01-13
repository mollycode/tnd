from django.shortcuts import render, redirect

from notes.models import Note

def my_notes(request):
    td = {}
    td["notes"] = Note.objects.all()
    
    return render(request, "my_notes.html", td)

def get_out(request):
    return redirect("main.views.home")
