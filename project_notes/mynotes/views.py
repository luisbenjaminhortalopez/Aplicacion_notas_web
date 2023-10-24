from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'note_list.html', {'notes': notes})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'note_detail.html', {'note': note})

def note_new(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'note_edit.html', {'form': form})

def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_edit.html', {'form': form})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('note_list')
