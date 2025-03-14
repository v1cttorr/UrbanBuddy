from django.shortcuts import redirect, render
from .models import Event, EventCategory
from .forms import EventForm

# Create your views here.
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