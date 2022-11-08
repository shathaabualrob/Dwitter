from django.contrib import admin
from django.contrib.auth.models import User,Group
from .models import Profile


# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"] # Only display the "username" field
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Profile)