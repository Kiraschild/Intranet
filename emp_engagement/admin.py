from django.contrib import admin
from emp_engagement.models import user_credentials,user_data, Event, TimeSheetData

# Register your models here.
admin.site.register(user_credentials)
admin.site.register(user_data)
admin.site.register(Event)
admin.site.register(TimeSheetData)