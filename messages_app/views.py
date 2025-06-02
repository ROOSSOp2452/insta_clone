from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Message
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Message
from django.db.models import Q, Max
from collections import defaultdict
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Max
from django.shortcuts import render
from .models import Message

@login_required
def inbox(request):
    user = request.user

    # Get all messages where user is sender or receiver
    messages = Message.objects.filter(Q(sender=user) | Q(receiver=user))

    # Build a dict: {other_user: latest_message}
    conversations = {}
    for msg in messages:
        other_user = msg.receiver if msg.sender == user else msg.sender
        if other_user not in conversations or conversations[other_user].timestamp < msg.timestamp:
            conversations[other_user] = msg

    # Sort by latest message timestamp
    sorted_conversations = sorted(conversations.items(), key=lambda item: item[1].timestamp, reverse=True)

    return render(request, 'messages_app/inbox.html', {
        'conversations': sorted_conversations,
    })


@login_required
def inbox_view(request):
    user = request.user

    # Find all unique conversation pairs where user is involved
    conversations = (
        Message.objects
        .filter(Q(sender=user) | Q(recipient=user))  # ✅ Changed 'receiver' to 'recipient'
        .values('sender', 'recipient')              # ✅ Changed 'receiver' to 'recipient'
        .annotate(last_msg_time=Max('timestamp'))
        .order_by('-last_msg_time')
    )

    recent_messages = []
    seen_users = set()

    for convo in conversations:
        # Identify the other participant
        other_user_id = convo['recipient'] if convo['sender'] == user.id else convo['sender']  # ✅ Changed
        if other_user_id in seen_users:
            continue
        seen_users.add(other_user_id)

        last_message = Message.objects.filter(
            Q(sender_id=user.id, recipient_id=other_user_id) |     # ✅ Changed
            Q(sender_id=other_user_id, recipient_id=user.id)       # ✅ Changed
        ).order_by('-timestamp').first()

        if last_message:
            recent_messages.append(last_message)

    return render(request, 'messages_app/inbox.html', {
        'messages': recent_messages,
    })



def conversation(request, username):
    other_user = get_object_or_404(User, username=username)
    user = request.user

    # Fetch all messages between the logged-in user and the other user
    messages = Message.objects.filter(
        sender__in=[user, other_user],
        recipient__in=[user, other_user]
    ).order_by('timestamp')

    if request.method == "POST":
        body = request.POST.get('body')
        if body:
            Message.objects.create(sender=user, recipient=other_user, body=body)
            return redirect('conversation', username=other_user.username)

    return render(request, 'messages_app/conversation.html', {
        'other_user': other_user,
        'messages': messages
    })

@login_required
def chat_view(request, username):
    receiver = User.objects.get(username=username)
    messages_list = Message.objects.filter(
        sender__in=[request.user, receiver],
        receiver__in=[request.user, receiver]
    ).order_by('timestamp')

    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Message.objects.create(sender=request.user, receiver=receiver, text=text)
            return redirect('chat_view', username=username)

    return render(request, 'messages_app/chat.html', {
        'username': username,
        'messages_list': messages_list
    })
    

def start_conversation(request):
    username = request.GET.get('username')
    if username:
        recipient = get_object_or_404(User, username=username)
        return redirect('messages_app:chat_view', username=recipient.username)
    return redirect('messages_app:inbox')