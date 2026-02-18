from django.shortcuts import render

# Create your views here.
from .utils import get_germini



"""def chat_view(request):
    if 'chat_history' not in request.session:
        request.session['chat_history'] = []

    if request.method == "POST":
        user_message = request.POST.get("user_message")
        bot_response = get_germini(user_message)
        request.session["chat_history"].append({
             'user': user_message,
            'bot': bot_response,

        })
        request.session.modified = True
    chat_history = request.session.get("chat_history",[])

    return render(request, 'chat_bot.html', {'chat_history': chat_history})

"""

def chat_view(request):
    # Initialize the chat history if not already in the session
    if 'chat_history' not in request.session:
        request.session['chat_history'] = []

    if request.method == "POST":
        # Get the user's message
        user_message = request.POST.get("user_message")
        
        # Get the response from the Harry Spooter model
        bot_response = get_germini(user_message)
        
        # Save the user's message and bot response to the session
        request.session['chat_history'].append({
            'user': user_message,
            'bot': bot_response,
        })
        
        # Save session data
        request.session.modified = True

    # Get the chat history from the session
    chat_history = request.session.get('chat_history', [])

    return render(request, 'chat_bot.html', {'chat_history': chat_history})


















