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
    # event_categorys = EventCategory.objects.all()
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
        # 'event_categorys': event_categorys,
        'events': events,
        'form': form,
    }

    return render(request, 'events/events.html', context)

def event(request, pk):
    event = Event.objects.get(id=pk)

    context = {
        'event': event,
    }

    return render(request, 'events/event.html', context)