from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PersonForm
from django.shortcuts import render
from Dental_GDU.models import Person, Note
from django.shortcuts import redirect, get_object_or_404
from .forms import NoteForm


# Create your views here.
def registration_view(request):
    # Logic for the patient registration screen
    # Retrieve form data, validate, and save to the database
    return render(request, 'Dental_GDU/registration.html')

def patient_details_view(request, patient_id):
    # Logic for the patient details screen
    # Retrieve patient data based on the patient_id and pass it to the template
    return render(request, 'Dental_GDU/patient_details.html', {'patient_id': patient_id})
    
def hello_view(request):
    return HttpResponse("Hello, world")


def home(request):
    return render(request, 'home.html')
    
def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page or any other desired page
    else:
        form = PersonForm()
    return render(request, 'add_person.html', {'form': form})

def add_note(request):
    if request.method == 'POST':
        # Process the form submission and save the note
        person_id = request.POST.get('person_id')
        content = request.POST.get('content')
        person = Person.objects.get(id=person_id)
        note = Note.objects.create(person=person, content=content)
        # Handle any additional logic or redirection

    # Fetch the list of persons to populate the dropdown
    persons = Person.objects.all()

    return render(request, 'add_note.html', {'persons': persons})
    
def view_notes(request):
    users = Person.objects.all()
    user = None
    notes = None

    if 'user' in request.GET:
        user_id = request.GET['user']
        user = Person.objects.get(id=user_id)
        notes = Note.objects.filter(person=user)

    context = {
        'users': users,
        'user': user,
        'notes': notes
    }

    return render(request, 'view_notes.html', context)
    



def update_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('view_notes')
    else:
        form = NoteForm(instance=note)

    return render(request, 'update_note.html', {'form': form})