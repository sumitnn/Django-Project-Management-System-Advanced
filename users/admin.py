from django.contrib import admin
from .models import CreateAccount, Project
from django.contrib.auth.admin import UserAdmin


# Register your models here.


admin.site.register(CreateAccount, UserAdmin)
UserAdmin.fieldsets += ("Additional ",
                        {'fields': ('profile_img', 'bio', 'mobile', 'gender', 'website', 'github', 'fb', 'insta', 'linkedin')}),

admin.site.register(Project)
