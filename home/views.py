from django.shortcuts import render, HttpResponse,redirect
from .models import Book, Topic

# Create your views here.

def say_hello(request):
    topics=Topic.objects.all()
    if "id" in request.GET:
        books=Book.objects.filter(topic=request.GET["id"])
    else:
        
        books= Book.objects.all()
    return render(request, "home/index.html", {"books":books, "topics":topics})
    
def add_topic(request):
    return render(request, "home/add_topic.html")
    
def add_topic_for_real(request):
    
    
    
    t=Topic()
    t.name=request.POST['topic']
    t.save()
    
    
    return redirect("/")
    
   
    
    