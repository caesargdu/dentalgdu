from django.shortcuts import render
from your_app.models import Person, Note

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
