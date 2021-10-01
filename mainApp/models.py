from django.db import models
import random

#======================== 
# Models 
# =======================

# Employee code is the required argument for creating supervisor
class Supervisors(models.Model):
	supervisor  		= models.CharField(max_length=100)

	def __str__(self):
		return self.supervisor
	
	class Meta:
		verbose_name_plural = "Supervisors"

class Employee(models.Model):
	first_name 			= models.CharField(max_length=100)
	middle_name			= models.CharField(max_length=100)
	date_of_graduation 	= models.DateTimeField()
	date_of_employment  = models.DateTimeField()
	position 			= models.CharField(max_length=100)
	salary 				= models.IntegerField()
	supervisors 		= models.ManyToManyField(Supervisors, blank=True)
	employee_code 		= models.CharField(max_length=6,blank=True, null=True)
	
	def save(self, *args, **kwargs):
		getThreeRandomNumbers   	  	= "".join(random.choice("0123456789") for i in range(3))
		generatedEmployeeCode  			= self.first_name[:1]+self.middle_name[:1]+'-'+getThreeRandomNumbers
		self.employee_code 				= generatedEmployeeCode
		super().save(*args, **kwargs)

	def __str__(self):
		return f"{self.first_name+self.middle_name}"

	class Meta:
		verbose_name_plural = "Employee Records"


class UploadLogs(models.Model):
	employee 							= models.ForeignKey(Employee, on_delete=models.CASCADE)
	timestamp_of_upload 				= models.DateTimeField(auto_now_add=True)
	number_of_employee_records_uploaded = models.IntegerField()
	status 								= models.CharField(max_length=100)
	errors 								= models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return f"{self.employee.employee_code}"

	class Meta:
		verbose_name_plural = "Upload logs"


