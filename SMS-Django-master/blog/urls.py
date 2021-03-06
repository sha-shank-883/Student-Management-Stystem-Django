from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("student/", views.student, name="student"),
    path("update/", views.update, name="update"),
    path("delete/", views.delete, name="delete"),
    # path("deletefn/", views.deletefn, name="deletefn"),
    path("about/", views.about, name="about"),
    path("service/", views.service, name="service"),
    path("contact/", views.contact, name="contact"),
    path("feedback/", views.feedback, name="feedback"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
