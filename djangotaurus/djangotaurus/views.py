from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_GET, require_POST
import re


@require_GET
def home(request):
    return render(request, 'index.html')


@require_POST
def search(request):
    if request.method == "POST":
        searchterm = str(request.POST.get('search'))
        if searchterm:
            return render(request, "search.html", {'searchterm': searchterm})
    return redirect(home)


@require_safe
def validate(searchterm):
    text_regex = r"([a-zA-Z]+\s)*[a-zA-Z]{1,255}$"
    if re.match(text_regex, searchterm):
        return True
    return False
