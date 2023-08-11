from typing import List

from django.shortcuts import render

# from services import generate_fruits, generate_vegetables, main


def index(request):
    users_name = []
    if request.method == "POST":
        name = request.POST.get("participant")
        users_name.append("name")
        return render(request, 'index.html', f'{name}')
    else:
        return render(request, "index.html")