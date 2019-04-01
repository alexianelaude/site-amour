from .models import Chat
from .forms import NewChat

def chat_infos(request):
    last_chats = Chat.objects.order_by('pub_date')[-25]
    chat_form = NewChat(request.POST or None)
    return {'last_chats': last_chats, 'chat_form': chat_form}