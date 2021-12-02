from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_safe
import re


@require_http_methods(["GET"])
def home(request):
    return render(request, 'index.html')


@require_http_methods(["POST"])
def search(request):
    if request.method == "POST":
        searchterm = str(request.POST.get('stock_id'))
        if searchterm:
            return render(request, "search.html", {'searchterm': searchterm})
    return render(request, 'index.html')


@require_safe
def validate(searchterm):
    text_regex = r"([a-zA-Z]+\s)*[a-zA-Z]{1,255}$"
    if re.match(text_regex, searchterm):
        return True
    return False
