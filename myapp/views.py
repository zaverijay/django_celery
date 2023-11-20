from django.shortcuts import render
from myceleryproject.celery import add
from myapp.tasks import sub
# Create your views here.

def index(request):
    # print("Results: ")
    result = add.delay(10, 20)
    print(result)
    return render(request, "myapp/home.html", {'result': result})


def about(request):
    result = sub.delay(20, 16)
    print("Results: ", result)
    return render(request, "myapp/about.html")


def contact(request):
    print("Results: ")
    return render(request, "myapp/contact.html")
