from django.urls import path
from .import views
app_name = "mainApp"

urlpatterns = [
	path("", views.EmployeeListView ,name="list-employees"),
	path("add-employee", views.AddEmployeeView, name="add-employee"),
	path("upload-logs", views.UploadLogs, name="logs-employees")
]