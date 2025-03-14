from django.shortcuts import redirect, render
from .models import Transport, TransportThroughLocation
from .forms import TransportForm
from accounts.models import Profile

# Create your views here.
def transports(request):
    transports = Transport.objects.all()

    data = {
        'user': Profile.objects.get(user=request.user)
    }

    form = TransportForm(data)

    if request.method == 'POST':
        form = TransportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transports')

    context = {
        'transports': transports,
        'form': form,
    }
    return render(request, 'transport/transports.html', context)

def transport(request, pk):
    transport = Transport.objects.get(pk=pk)
    locations = TransportThroughLocation.objects.filter(transport=transport)

    context = {
        'transport': transport,
        'locations': locations
    }
    return render(request, 'transport/transport.html', context)