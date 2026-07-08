from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    isActive = True
    if request.method == 'POST':
        check = request.POST.get('check')
        print(check)
        if check is None: isActive = False
        else: isActive = True
    date = datetime.datetime.now()
    name = "themadhurima"
    list_of_programs = [
        'WAP to check even or odd',
        'WAP to check prime numbers',
        'WAP to print all prime numbers from 1 to 100',
        'WAP to print pascals triangle'
    ]
    student = {
        'student_name': "Madhurima",
        'student_college': "XYZ",
        'student_city': "Lucknow"
    }
    data = {
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student

    }
    # return HttpResponse("<h1>Hello this is index page<h1>" + str(date))
    return render(request, 'home.html',data)
def about(request):
    # return HttpResponse("<h1> This is about page<h1>")
    return render(request, 'about.html', {})
def service(request):
    # return HttpResponse("<h1> This is service page<h1>")
    return render(request, 'service.html', {})
