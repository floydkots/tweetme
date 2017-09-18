from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Tweet

# Create your views here.


# Retrieve tweet

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    template_name = "tweets/detail_view.html"

    def get_object(self):
        return Tweet.objects.get(id=1)


class TweetListView(ListView):
    template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()

def tweet_detail_view(request, id=1):
    obj = Tweet.objects.get(id=id)  # Get from database
    context = {
        "object": obj
    }
    return render(request, "tweets/detail_view.html", context)


# List tweets
def tweet_list_view(request):
    queryset = Tweet.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "tweets/list_view.html", context)
