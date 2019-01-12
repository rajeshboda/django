# function views
import random
from django.http import HttpResponse


def hello(request):
    return HttpResponse('<h1>Hello Django</h1>')


def myHello(request):
    return HttpResponse('<h2> Are you kidding!!</h2>')


def result(request):
    random_number = random.randrange(1, 100, 2)
    print("Random number is ", random_number)
    if random_number < 35:
        result = "you are  fail  :( "
    elif random_number == 35:
        result = "You just passed :|"
    elif random_number > 35 and random_number <= 60:
        result = "You are average student :)"
    elif random_number > 60 and random_number <= 80:
        result = "you got Distinction!! Congrats ;-)"
    else:
        result = "Oh Man, You are a beast!!"

    if 'name' in request.GET:
        name = request.GET["name"]
    else:
        name = "unknown user"
    return HttpResponse(f'<h3> Hey {name} ! {result} </h3>')
