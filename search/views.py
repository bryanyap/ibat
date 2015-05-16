from django.shortcuts import render
from .models import Employee

# Create your views here.
def index(request):
    employee_list = Employee.objects.order_by('name')[:5]
    context = {'employee_list': employee_list}
    return render(request, 'search/search_template.html', context)
