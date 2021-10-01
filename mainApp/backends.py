from .models import Employee 

# Logical functions

def ValidateSupervisorCreation(get_employee_code):
	if Employee.objects.filter(employee_code=get_employee_code).exists():
		employee 	= Employee.objects.get(employee_code=get_employee_code)
		return employee.first_name+employee.middle_name
	else:
		return None
	