from django.shortcuts import render
from django.conf import settings
from django.utils.safestring import mark_safe
import google.generativeai as genai
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# required models
from accounts.models import Profile
from events.models import Event

from .forms import ChatBotPromptForm

# Create your views here.
@login_required
def interests_ideas(request):
    api_key = settings.API_KEY
    
    if not api_key:
        raise ValueError("API_KEY not set")
    
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.0-flash")

    user_interests = Profile.objects.get(user=request.user).interests

    response = model.generate_content(f'I\'m interested in this things  {user_interests} give me 3 ideas what I can do with it (points only) (if not specified generate random ideas)')
    
    formatted_response = mark_safe(response.text.replace("*", " "))

    return formatted_response

@login_required
def event_ideas(request):
    api_key = settings.API_KEY
    
    if not api_key:
        raise ValueError("API_KEY not set")

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.0-flash")
    
    events = ", ".join(Event.objects.filter(user=request.user).values_list('title', flat=True))
    
    response = model.generate_content(f'I had taken part in these events {events} give me 3 ideas for the next event (points only)')
    
    formatted_response = mark_safe(response.text.replace("*", " "))

    return formatted_response

@login_required
def chat_bot(request):
    api_key = settings.API_KEY
    
    if not api_key:
        raise ValueError("API_KEY not set")

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('gemini-2.0-flash-lite')
    
    if request.method == 'POST':
        form = ChatBotPromptForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']
            response = model.generate_content(prompt)
            formatted_response = mark_safe(response.text.replace("*", " "))
            return render(request, 'gpt/chat_bot.html', {'form': form, 'response': formatted_response})
    else:
        form = ChatBotPromptForm()
        response = ''
    return render(request, 'gpt/chat_bot.html', {'form': form, 'response': f'{response}'})