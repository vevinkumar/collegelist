from django.contrib import admin
from colleges.models import UserList, CollegeList

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'password')
    search_fields = ['user_name']
	
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('college_id', 'college_name', 'district', 'image1', 'image2', 'image3')
    search_fields = ['college_id', 'college_name', 'district']
	
admin.site.register(UserList, UserAdmin)
admin.site.register(CollegeList, CollegeAdmin)