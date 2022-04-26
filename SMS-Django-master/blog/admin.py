from django.contrib import admin

# from blog.views import delete
from .models import About, Contact, Feedback, Student

# admin.site.register(Student)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(Student)
# admin.site.register(Delete)
# admin.site.register(Update)
