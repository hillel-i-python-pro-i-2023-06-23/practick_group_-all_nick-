from typing import List

from django.shortcuts import render

# from services import generate_fruits, generate_vegetables, main


def index(request):
    users_name = []
    if request.method == "POST":
        names = request.POST.getlist("participant")

        for name in names:
            users_name.append(name)

        # Добавили в index.html вывод списка имен игроков:
        return render(request, 'index.html', {"names": names})
    else:
        return render(request, "index.html")