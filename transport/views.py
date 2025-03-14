from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Transport, TransportThroughLocation, TransportRequest
from .forms import TransportForm
from accounts.models import Profile

# Create your views here.
def transports(request):
    transports = Transport.objects.all()

    form = TransportForm()

    if request.method == 'POST':
        form = TransportForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = Profile.objects.get(user=request.user)
            instance.save()
            
            locations = request.POST.getlist('locations')
            print(locations)

            for location in locations:
                transport_through_location = TransportThroughLocation.objects.create(
                    transport=instance,
                    location=location
                )
                transport_through_location.save()
            return redirect('transports')

    context = {
        'transports': transports,
        'form': form,
    }
    return render(request, 'transport/transports.html', context)

def transport(request, pk):
    transport = Transport.objects.get(pk=pk)
    locations = TransportThroughLocation.objects.filter(transport=transport)

    if request.method == 'POST':
        message = request.POST.get('message')
        user = Profile.objects.get(user=request.user)
        transport_request = TransportRequest.objects.create(
            user=user,
            transport=transport,
            message=message
        )
        transport_request.save()

        return redirect('transport', pk=pk)

    context = {
        'transport': transport,
        'locations': locations
    }
    return render(request, 'transport/transport.html', context)

def requests(request):
    user = Profile.objects.get(user=request.user)
    transport_requests = TransportRequest.objects.filter(transport__user=user)

    context = {
        'transport_requests': transport_requests
    }

    return render(request, 'transport/requests.html', context)

def accept_request(request, pk):
    transport_request = TransportRequest.objects.get(pk=pk)
    transport_request.accepted = True
    transport_request.save()
    return redirect('requests')