from .models import Chat
from .forms import NewChat

def chat_infos(request):
    last_chats = Chat.objects.order_by('-pub_date')[:8]
    form = NewChat(request.POST or None)
    return {'last_chats': last_chats, 'form': form}