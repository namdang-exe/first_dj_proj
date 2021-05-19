from django.shortcuts import render

tasks = ["eat", "sleep", "code"]


# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
