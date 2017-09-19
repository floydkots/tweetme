from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.views.generic import (DetailView,
                                  ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)

from .forms import TweetModelForm
from .models import Tweet
from .mixins import FormUserNeededMixin, UserOwnerMixin


class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    # success_url = reverse_lazy("tweet:detail")
    login_url = '/admin/'


# Update views

class TweetUpdateView(UserOwnerMixin, LoginRequiredMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    # success_url = "/tweet/"
    template_name = 'tweets/update_view.html'


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    success_url = reverse_lazy("tweet:list")
    template_name = "tweets/delete_confirm.html"


def tweet_create_view(request):
    form = TweetModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()

    context = {
        "form": form
    }
    return render(request, 'tweets/create_view.html', context)


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    template_name = "tweets/detail_view.html"


class TweetListView(ListView):
    template_name = "tweets/list_view.html"

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(Q(content__icontains=query) |
                           Q(user__username__icontains=query))
        return qs

    def get_context_data(self, **kwargs):
        context = super(TweetListView, self).get_context_data(**kwargs)
        return context


def tweet_detail_view(request, pk=None):
    obj = get_object_or_404(Tweet, pk=pk)  # Get from database
    context = {
        "object": obj
    }
    return render(request, "tweets/detail_view.html", context)


def tweet_list_view(request):
    queryset = Tweet.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "tweets/list_view.html", context)
