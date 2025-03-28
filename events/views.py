from django.shortcuts import redirect, render
from .models import Event
from .forms import EventForm
from gpt.views import interests_ideas, event_ideas
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        interests  = interests_ideas(request)
        events = event_ideas(request)
        
        return render(request, 'home.html', {'interests': interests, 'events': events})
    return render(request, 'home.html')

@login_required
def events(request):
    events = Event.objects.all().order_by('-date', 'category')

    form = EventForm()

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('events')

    if request.method == 'GET':
        search = request.GET.get('search')
        if search:
            events = Event.objects.filter(title__icontains=search).order_by('-date', 'category')

    context = {
        'events': events,
        'form': form,
    }

    return render(request, 'events/events.html', context)

@login_required
def event(request, pk):
    event = Event.objects.get(id=pk)

    context = {
        'event': event,
    }

    return render(request, 'events/event.html', context)