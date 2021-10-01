from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
# Create your views here.

def EmployeeListView(request):
	employees  				= Employee.objects.all()
	
	context = {
		"employees":employees,
	}

	return render(request, 'employee-list.html',context)

def AddEmployeeView(request):
	return render(request, 'add-employee.html')

def UploadLogs(request):
	return render(request, 'employee-logs.html')