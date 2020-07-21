'''
from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Note
# Create your views here.
def home(request):
    notes = Note.objects
    template = loader.get_template('note.html')
    context = {'notes': notes}
    return render(request, 'note.html', context)
#return render_to_response("note.html", notes)
'''
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm

# Create your views here.

def home(request):
    notes = Note.objects
    template = loader.get_template('note.html')
    form = NoteForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    context = {'notes': notes, 'form': form}
    return render(request, 'note.html', context)
    #return render_to_response("note.html", notes)


from django.shortcuts import redirect
from .forms import RegisterForm


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/note.html")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})
