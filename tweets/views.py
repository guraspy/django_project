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
    # TODO[DG] data = reversed(data) gasarkvevia listad rato gadavaqcie

    # TODO egreve listi ro gadavce da ara dict
    tweets = {
        "tweets": data,
    }
    
    return render(request, "pages/home.html", tweets)

@login_required
def tweet_create_view(request, *args, **kwargns):
    # if request.method == 'POST':
        form = TweetForm(request.POST or None, request.FILES or None)
        context={"form": form,}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            form = TweetForm()
            context = {"form": form,
                        "response": "tweet succesfully posted"}
    # else:
    #     form = TweetForm()      
    #     context = {}
        return render(request, "tweets/forms.html", context)

# TODO[DG] find_tweet_by_id
def all_tweet_view(request, tweet_id, *args, **kwargs):
    tweet = {
        "id": tweet_id,
    } 
    try:
        obj = Tweet.objects.get(id=tweet_id)
        tweet["content"] = obj.content
    except:
        return render(request, "errors/tweet-error.html", tweet)

    return render(request, "pages/tweet-page.html", tweet)


@login_required
def tweet_view(request, *args, **kwargs): 

    data = Tweet.objects.all().filter(user_id=request.user.pk)
    
    # reversing data to display new tweets first
    tweets = {    
        "tweets": reversed(data)
    } 
    
    return render(request, "pages/user-tweets.html", tweets)


@login_required
def delete_tweet(request, tweet_id, *args, **kwargs):

    post_to_delete=Tweet.objects.get(id=tweet_id)
    post_to_delete.delete()

    return render(request, "pages/delete-tweet.html")


def search_tweet(request):


    if request.method == "POST":
        searched = request.POST['searched']
        tweets = Tweet.objects.filter(content__contains=searched)

        return render(request, "pages/search-tweets.html",
                                 {'searched':searched,
                                'tweets':tweets,
                                'user':request.user})

    else:
        return render(request, "pages/search-tweets.html", {})

@login_required
def about(request):
    
    return render(request, "pages/about.html", {'user': request.user})