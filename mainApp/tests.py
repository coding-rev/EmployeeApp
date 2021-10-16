import datetime
import pytz
from django.test import TestCase
from .models import Employee, Supervisors, UploadLogs


# Create your tests here.
class ModelsTest(TestCase):

	def test_employee_creation(self):
		employee = Employee.objects.create(first_name="Emmanuel", middle_name="Owusu",
								date_of_graduation=datetime.datetime.now(pytz.utc),
								date_of_employment=datetime.datetime.now(pytz.utc),
								position="Software Engineer", salary="5000")
		employee.save()
		self.assertEqual(employee.first_name, "Emmanuel")
		self.assertEqual(employee.middle_name, "Owusu")

	def test_supervisor_creation(self):
		employee = Employee.objects.create(first_name="Emmanuel", middle_name="Owusu",
								date_of_graduation=datetime.datetime.now(pytz.utc),
								date_of_employment=datetime.datetime.now(pytz.utc),
								position="Software Engineer", salary="5000")
		employee.save()

		employeeKey = employee.first_name+employee.middle_name
		supervisor = Supervisors.objects.create(supervisor=employeeKey)
		supervisor.save()
		self.assertEqual(supervisor.supervisor, employeeKey)

	def test_upload_logs(self):
		log 	= UploadLogs.objects.create(timestamp_of_upload=datetime.datetime.now(pytz.utc),
								number_of_employee_records_uploaded=5, status="success", number_of_duplicate_entries=0)
		log.save()
		self.assertEqual(log.status, "success")

	





