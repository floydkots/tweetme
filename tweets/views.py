from django.shortcuts import render

# Create your views here.


# Retrieve tweet
def tweet_detail_view(request, id=1):
    return render(request, "tweets/detail_view.html", {})


# List tweets
def tweet_list_view(request):
    return render(request, "tweets/list_view.html", {})