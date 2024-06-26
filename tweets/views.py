from django.shortcuts import redirect, render
from .models import Tweet, LikePost
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

def find_tweet_by_id(request, tweet_id, *args, **kwargs):
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

@login_required
def like_tweet(request):
    username = request.user.username
    tweet_id = request.GET.get('tweet_id')
    
    tweet = Tweet.objects.get(id=tweet_id)
    
    like_filter = LikePost.objects.filter(tweet_id=tweet_id, username=username).first()
    
    if like_filter == None:
        new_like = LikePost.objects.create(tweet_id=tweet_id, username=username)
        new_like.save()
        print(dir(tweet))
        tweet.no_of_likes = tweet.no_of_likes + 1
        tweet.save()
        return redirect('/')
    else:
        like_filter.delete()
        tweet.no_of_likes = tweet.no_of_likes - 1
        tweet.save()
        return redirect('/')