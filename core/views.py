import hashlib

from django.db.models import F
from django.shortcuts import get_object_or_404, redirect, render
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
        url = form.cleaned_data["url"]
        code = hashlib.md5(url.encode(), usedforsecurity=False).hexdigest()[:8]
        entry, _ = Entry.objects.get_or_create(code=code, defaults={"url": url})
        return redirect(entry)
    # FIXME: this doesn't work, as there's no shorten template
    return render(request, "core/shorten.html", {"form": form})


def redirect_entry(request, code):
    entry = get_object_or_404(Entry, code=code)
    entry.hits = F("hits") + 1
    entry.save()
    return redirect(entry.url)


def detail(request, code):
    entry = get_object_or_404(Entry, code=code)
    return render(request, "core/detail.html", {"entry": entry})


@require_POST
def delete(request, code):
    entry = get_object_or_404(Entry, code=code)
    entry.delete()
    return redirect(reverse("home"))
