from django.shortcuts import redirect, render
from .models import Event, EventCategory
from .forms import EventForm
from gpt.views import interests_ideas

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        interests  = interests_ideas(request)
        
        return render(request, 'home.html', {'interests': interests})
    return redirect('/login')

def events(request):
    event_categorys = EventCategory.objects.all()

    form = EventForm()

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('events')

    context = {
        'event_categorys': event_categorys,
        'form': form,
    }

    return render(request, 'events/events.html', context)

def event(request, pk):
    event = Event.objects.get(id=pk)

    context = {
        'event': event,
    }

    return render(request, 'events/event.html', context)