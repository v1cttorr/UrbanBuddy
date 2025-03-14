from django.shortcuts import render
from django.conf import settings
from django.utils.safestring import mark_safe
import google.generativeai as genai
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# required models
from accounts.models import Profile
from events.models import Event

# Create your views here.
@login_required
def interests_ideas(request):
    user_interests = Profile.objects.get(user=request.user).interests
    
    if len(user_interests) < 1:
        return 'Please add your interests in your profile'
    api_key = settings.API_KEY
    
    if not api_key:
        raise ValueError("API_KEY not set")
    
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.0-flash")

    response = model.generate_content(f'I\'m interested in this things  {user_interests} give me 3 ideas what I can do with it (points only) (if not specified generate random ideas)')
    
    formatted_response = mark_safe(response.text.replace("*", " "))

    return formatted_response

@login_required
def event_ideas(request):
    events = ", ".join(Event.objects.filter(user=request.user).values_list('title', flat=True))

    if len(events) < 1:
        return 'You don\' have any events added yet, please add some'
    
    api_key = settings.API_KEY
    
    if not api_key:
        raise ValueError("API_KEY not set")

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.0-flash")
    
    
    response = model.generate_content(f'I had taken part in these events {events} give me 3 ideas for the next event (points only)')
    
    formatted_response = mark_safe(response.text.replace("*", " "))

    return formatted_response

