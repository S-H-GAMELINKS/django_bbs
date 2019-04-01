from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from .forms import CommentsForm, TopicsForm
from .models import Comment, Topic

def index(request):
    topics = Topic.objects.all()
    return HttpResponse(render(request, 'topics/index.html', {'topics': topics, 'topics_form': TopicsForm}))

def detail(request, topic_id):
    try:
        topic = Topic.objects.get(pk=topic_id)
        comments = Comment.objects.all()
    except Topic.DoesNotExist:
        raise Http404("Topic does not Exist!")
    return render(request, 'topics/detail.html', {'topic': topic, 'comments': comments, 'comments_form': CommentsForm})

def create(request):
    topic = Topic.objects.create(title_text=request.POST['title_text'], content_text=request.POST['content_text'])
    return redirect('detail', topic_id=topic.id)

def comments(request, topic_id):
    topic = Topic.objects.get(pk=topic_id)
    Comment.objects.create(topic=topic, content_text=request.POST['content_text'])
    return redirect('detail', topic_id=topic_id)