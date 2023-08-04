from django.shortcuts import HttpResponse

# Create your views here.


def greetings(request, name: str, age: int):
    return HttpResponse(f"hello!, {name}, age: {age}")
