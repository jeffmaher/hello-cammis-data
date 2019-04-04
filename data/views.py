from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from data.models import Greeting
from data import controller

def hello(request, name):
    greeting = get_object_or_404(Greeting, name=name)
    return JsonResponse({'hello': greeting.greeting + greeting.punctuation})

@csrf_exempt
def add_greeting(request, name):
    # Parse input
    try:
        greeting_str = request.POST['greeting']
    except:
        return HttpResponseBadRequest(reason="Missing 'greeting' from form-data")
    
    # Save the Greeting
    greeting = controller.add_greeting(name, greeting_str)
    if greeting:
        return JsonResponse({'name': greeting.name, 'greeting': greeting.greeting, 'punctuation': greeting.punctuation})

    # If the Greeting couldn't be saved
    return HttpResponseServerError("Trouble saving the Greeting. Sorry!")

def alive(request):
    # Nothing else to check internally, aside from being able to receive a request
    return HttpResponse("Alive and healthy!")

def ready(request):
    # Success
    if ready_database():
        return HttpResponse("System is ready for traffic!")
    
    # Fail
    return HttpResponseServerError("Database is not ready")

def ready_database():
    # Save a record to the database
    unlikely_name = "jkadfsjk3jl2"
    if controller.add_greeting(unlikely_name, "Ready", "!") == None:
        return False

    # Retrieve a record from the database
    return controller.get_greeting(unlikely_name)