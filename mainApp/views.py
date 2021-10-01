from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Employee, Supervisors
from .backends import ValidateSupervisorCreation

# Create your views here.

def EmployeeListView(request):
	employees  	= Employee.objects.all().order_by('first_name')
	context 	= {
		"employees":employees,
	}

	return render(request, 'employee-list.html',context)

def AddEmployeeView(request):
	employees 	= Employee.objects.all()
	context 	= {
		"employees":employees
	}
	# Taking form values on post
	if request.method =='POST':
		first_name    				=  request.POST.get('first_name')
		middle_name   				=  request.POST.get('middle_name')
		date_of_graduation     		=  request.POST.get('date_of_graduation')
		date_of_employment  		=  request.POST.get('date_of_employment')
		position					=  request.POST.get('position')
		salary						=  request.POST.get('salary')
		getSupervisors				=  request.POST.getlist('get_supervisor')
		
		try:
			employee 		= Employee.objects.create(
								first_name=first_name, middle_name=middle_name,
								date_of_graduation=date_of_graduation, 
								date_of_employment=date_of_employment, position=position,
								salary=salary)
			employee.save()

			# If no supervisor was selected
			if len(getSupervisors)==0:
				pass
			# If one or more supervisor(s) were selected
			else:
				for supervisor_code in getSupervisors:
					supervisor_key_name = ValidateSupervisorCreation(supervisor_code)
					# If the employee already have a supervisor account
					if Supervisors.objects.filter(supervisor=supervisor_key_name).exists():
						supervisor = Supervisors.objects.get(supervisor=supervisor_key_name)
						employee.supervisors.add(supervisor)

					# If the employee does not have a supervisor account
					else:
						supervisor = Supervisors.objects.create(supervisor=supervisor_key_name)
						supervisor.save()
						employee.supervisors.add(supervisor)
			
			messages.success(request, "Employee added successfully")
			return render(request, 'add-employee.html', context)

		except Exception as e:
			messages.error(request, str(e))
	return render(request, 'add-employee.html',context)

def UploadLogs(request):
	return render(request, 'employee-logs.html')







