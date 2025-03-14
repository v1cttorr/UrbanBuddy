from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Transport, TransportThroughLocation, TransportRequest
from .forms import TransportForm
from accounts.models import Profile
from transport.models import Alert


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

            for location in locations:
                transport_through_location = TransportThroughLocation.objects.create(
                    transport=instance,
                    location=location
                )
                transport_through_location.save()
            return redirect('transports')
        
    if request.method == 'GET':
        from_location = request.GET.get('from_location', "")
        destination = request.GET.get('destination', "")
        locations_search = request.GET.getlist('locations_search', "")
        
        transports = Transport.objects.filter(
                                                from_location__icontains=from_location,
                                                to_location__icontains=destination,
                                                transportthroughlocation__location__in=locations_search
                                              )
        print(from_location, destination, locations_search)

        context = {
            'transports': transports,
            'form': form,
        }
        return render(request, 'transport/transports.html', context)


    context = {
        'transports': transports,
        'form': form,
    }
    return render(request, 'transport/transports.html', context)

def transport(request, pk):
    transport = Transport.objects.get(pk=pk)
    locations = TransportThroughLocation.objects.filter(transport=transport)

    #ADD REQUEST
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

def map(request):
    alerts = Alert.objects.all()

    return render(request, 'transport/map.html', {'alerts': alerts})

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

    transport = transport_request.transport
    transport.passengers.add(transport_request.user)
    return redirect('requests')