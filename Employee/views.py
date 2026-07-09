from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Empower, Testimonial
# Create your views here.
def empower_home(request):
    employees = Empower.objects.all()
    return render(request, "empower/home.html", {
        "employees": employees
    })
def add_emp(request):
    if request.method == "POST":
        #print("data is coming")
        employee_name = request.POST.get("employee_name")
        employee_id = request.POST.get("employee_id")
        employee_phone = request.POST.get("employee_phone")
        employee_address = request.POST.get("employee_address")
        employee_working = request.POST.get("employee_working")
        employee_department = request.POST.get("employee_department")

        e = Empower()
        e.name = employee_name
        e.emp_ID = employee_id
        e.phone = employee_phone
        e.address = employee_address
        e.department = employee_department
        if employee_working is None:
            e.working = False
        else:
            e.working = True
        e.save()    
        return redirect("/empower/home/")
    return render(request, "empower/add_emp.html",{})
def delete_emp(request, emp_id):
    #print(emp_id)
    emp = Empower.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/empower/home/")
def update_emp(request, emp_id):
    emp = Empower.objects.get(pk=emp_id)
    return render(request, "empower/update_emp.html", {
        'emp': emp
    })
def do_update_emp(request, emp_id):
    if request.method == 'POST':
        employee_name = request.POST.get("employee_name")
        employee_id = request.POST.get("employee_id")
        employee_phone = request.POST.get("employee_phone")
        employee_address = request.POST.get("employee_address")
        employee_working = request.POST.get("employee_working")
        employee_department = request.POST.get("employee_department")
        e = Empower.objects.get(pk=emp_id)
        e.name = employee_name
        e.emp_ID = employee_id
        e.phone = employee_phone
        e.address = employee_address
        e.department = employee_department
        if employee_working is None:
            e.working = False
        else:
            e.working = True
        e.save()
    return redirect("/empower/home/")
def testimonials(request):
    testi = Testimonial.objects.all()

    return render(request, "empower/testimonials.html",{
        'testi':testi
    })