from django.contrib import admin
from .models import Employee, Supervisors, UploadLogs
# UploadLogs

# Customizing admin page
admin.site.site_title 	= "Employee Data Collation App | Admin"
admin.site.site_header 	= "EDCA | ADMIN"

# Registering models
class AdminEmployeeDisplay(admin.ModelAdmin):
	list_filter = ["position"]

class AdminUploadLogsDisplay(admin.ModelAdmin):
	list_display = ["employee","timestamp_of_upload","status"]
	
admin.site.register(Employee, AdminEmployeeDisplay) 
admin.site.register(UploadLogs, AdminUploadLogsDisplay)
admin.site.register(Supervisors)

