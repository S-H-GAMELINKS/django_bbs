from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from .forms import TopicsForm
from .models import Topic

def index(request):
    topics = Topic.objects.all()
    return HttpResponse(render(request, 'topics/index.html', {'topics': topics, 'topics_form': TopicsForm}))

def detail(request, topic_id):
    try:
        topic = Topic.objects.get(pk=topic_id)
    except Topic.DoesNotExist:
        raise Http404("Topic does not Exist!")
    return render(request, 'topics/detail.html', {'topic': topic})

def create(request):
    topic = Topic.objects.create(title_text=request.POST['title_text'], content_text=request.POST['content_text'])
    return redirect('detail', topic_id=topic.id)