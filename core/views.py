from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import Shorten


def shorten(request):
    if request.method == "POST":
        form = Shorten(request.POST)
        if form.is_valid():
            entry = form.save()
            messages.success(request, entry.code)
            return redirect("/shorten")
    else:
        form = Shorten()
    return render(request, "core/shorten.html", {"form": form})
