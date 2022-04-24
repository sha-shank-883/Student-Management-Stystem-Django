from django.contrib import admin

# from blog.views import delete
from .models import Student, About, Contact, Feedback, Insert, Update

admin.site.register(Student)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(Insert)
# admin.site.register(Delete)
admin.site.register(Update)
