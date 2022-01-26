from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.


admin.site.register(CreateAccount, UserAdmin)
UserAdmin.fieldsets += ("Additional ",
                        {'fields': ('profile_img', 'bio', 'mobile', 'gender', 'website', 'github', 'fb', 'insta', 'linkedin')}),


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title',
                    'current_time', 'project_img', 'project_file', 'description']


admin.site.register(Comment)
