from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from .forms import Shorten
from .models import Entry


def home(request):
    form = Shorten()
    entries = Entry.objects.all()
    return render(request, "core/home.html", {"form": form, "entries": entries})


@require_POST
def shorten(request):
    form = Shorten(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse("home"))
    return render(request, "core/shorten.html", {"form": form})
