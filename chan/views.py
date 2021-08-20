from django import template
from django.shortcuts import render
from .models import Thread, Respone, Board
from django.http import HttpResponse
from django.template import loader
from .forms import NewThread, Respond



def index(request):
    board_list = Board.objects.all()
    thread_list = Thread.objects.all()[:10]
    template = loader.get_template('chan/index.html')
    context = {
        'board_list': board_list,
        'thread_list': thread_list,
    }
    return HttpResponse(template.render(context, request))


def thread(request,thread_id):
    board_list = Board.objects.all()
    thread = Thread.objects.get(pk=thread_id)
    responses = Respone.objects.filter(t_id=thread_id)
    template = loader.get_template('chan/thread.html')
    form = Respond(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.t_id= thread
        obj.save()

    context = {
        'board_list' : board_list,
        'thread': thread,
        'responses': responses,
        'form': form, 
    }
    return HttpResponse(template.render(context, request))

def board(request, board_link):
    board_list = Board.objects.all()
    board = Board.objects.get(link=board_link)
    threads = Thread.objects.filter(board=board.id)
    template = loader.get_template('chan/board.html')

    form = NewThread(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.board = board
        obj.save()

    context = {
        'form' : form,
        'board_list' : board_list,
        'board': board,
        'thread_list' : threads
    }
    return HttpResponse(template.render(context, request))