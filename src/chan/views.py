from django import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import *
from .forms import *
# Create your views here.


def index(request):
    """View for main page/index."""
    site = SiteSettings.objects.all()[0]
    template = loader.get_template('index.html')
    boards = Board.objects.all()
    news = News.objects.all()[:10:-1]
    replies = Reply.objects.all().order_by('-date_posted')[:10]
    threads = []
    for i in replies:
        threads.append(Thread.objects.get(pk=i.t_id))
    threads = list(set(threads))
    context = {
        'site': site,
        'boards': boards,
        'threads': threads,
        'news': news,
    }
    return HttpResponse(template.render(context, request))


def board(request, board_url):
    site = SiteSettings.objects.all()[0]
    template = loader.get_template('board.html')
    boards = Board.objects.all()
    board = Board.objects.get(url=board_url)
    # this requires fixing, because its completelly wrong.
    sticky = Thread.objects.filter(b_id=board.id, is_sticky=True)
    threads = Thread.objects.filter(
        b_id=board.id, is_sticky=False).order_by('-date_posted')
    form = NewThread(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.b_id = board
        obj.save()

    context = {
        'site': site,
        'boards': boards,
        'board': board,
        'sticky': sticky,
        'threads': threads,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def thread(request, board_url, thread_id):
    site = SiteSettings.objects.all()[0]
    boards = Board.objects.all()
    template = loader.get_template('thread.html')
    thread = Thread.objects.get(pk=thread_id)
    board = Board.objects.get(url=board_url)
    replies = Reply.objects.filter(t_id=thread.id)
    form = NewReply(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.t_id = thread
        obj.save()
    context = {
        'site': site,
        'board': board,
        'thread': thread,
        'boards': boards,
        'replies': replies,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def news(request, news_id):
    site = SiteSettings.objects.all()[0]
    boards = Board.objects.all()
    template = loader.get_template('news.html')
    news = News.objects.get(pk=news_id)
    context = {
        'site': site,
        'boards': boards,
        'news': news,
    }
    return HttpResponse(template.render(context, request))


def newslist(request):
    site = SiteSettings.objects.all()[0]
    boards = Board.objects.all()
    template = loader.get_template('newslist.html')
    news = News.objects.all()
    context = {
        'site': site,
        'boards': boards,
        'news': news,
    }
    return HttpResponse(template.render(context, request))


def rules(request):
    site = SiteSettings.objects.all()[0]
    boards = Board.objects.all()
    template = loader.get_template('rules.html')
    rules = Rule.objects.all()
    context = {
        'site': site,
        'boards': boards,
        'rules': rules,
    }
    return HttpResponse(template.render(context, request))


def faq(request):
    site = SiteSettings.objects.all()[0]
    boards = Board.objects.all()
    template = loader.get_template('faq.html')
    faqs = FaqQuestion.objects.all()
    context = {
        'site': site,
        'boards': boards,
        'faqs': faqs,
    }
    return HttpResponse(template.render(context, request))
