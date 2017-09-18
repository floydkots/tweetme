from django.conf.urls import url

from .views import tweet_detail_view, tweet_list_view

from tweets.views import TweetDetailView, TweetListView

urlpatterns = [
    url(r'^$', TweetListView.as_view(), name='list'),
    url(r'^1/$', TweetDetailView.as_view(), name='detail')
]



