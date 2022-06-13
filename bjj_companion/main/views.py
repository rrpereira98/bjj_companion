import imp
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.

def home(response):
	return render(response, "main/home.html", {})

def create_tournment(request):
    participants = Participant.objects.all()

    form = ParticipantForm()

    if request.method == "POST":
        if "Create_Participant" in request.POST:
            form = ParticipantForm(request.POST)
            if form.is_valid:
                form.save()
            return redirect("/create_tournment/")

    context = {"participants":participants, "form":form}
    return render(request, "main/create_tournment.html", context)