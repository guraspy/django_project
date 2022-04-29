from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse_lazy
from .models import Tweet, User
from .forms import TweetForm
from django.contrib.auth.decorators import login_required


@login_required
def home_view(request, *args, **kwargs):

    data = Tweet.objects.all()

    # reversing data to display new messages first
    data = list(reversed(data))

    messages = {
        "messages": data,
        "user": request.user
    }
    
    return render(request, "pages/home.html", messages)

@login_required
def message_create_view(request, *args, **kwargns):
    form = TweetForm(request.POST or None)
    context={"form": form,}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = TweetForm()
        context = {"form": form,
                    "response": "message succesfully posted"}
        
    return render(request, "messages/forms.html", context)

def all_message_view(request, tweet_id, *args, **kwargs):
    print(dir(request))
    message = {
        "id": tweet_id,
    } 
    try:
        obj = Tweet.objects.get(id=tweet_id)
        message["content"] = obj.content
    except:
        return render(request, "errors/message-error.html", message)

    return render(request, "pages/tweet-page.html", message)

@login_required
def message_view(request, *args, **kwargs): 

    data = Tweet.objects.all().filter(user_id=request.user.pk)
    
    # reversing data to display new messages first
    messages = {    
        "messages": reversed(data)
    } 
    
    return render(request, "pages/user-messages.html", messages)

@login_required
def delete_message(request, tweet_id, *args, **kwargs):

    post_to_delete=Tweet.objects.get(id=tweet_id)
    post_to_delete.delete()

    return render(request, "pages/delete-message.html")


def search_message(request):


    if request.method == "POST":
        searched = request.POST['searched']
        messages = Tweet.objects.filter(content__contains=searched)

        return render(request, "pages/search-messages.html",
                                 {'searched':searched,
                                'messages':messages,
                                'user':request.user})

    else:
        return render(request, "pages/search-messages.html", {})

@login_required
def about(request):
    
    return render(request, "pages/about.html", {'user': request.user})