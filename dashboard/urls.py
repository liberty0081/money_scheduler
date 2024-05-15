from django.urls import path

from . import views

app_name = "dashboard"
urlpatterns = [
    path("", views.index, name="index"),
    path("form/", views.form, name="form"),
    path("update/<int:outcome_id>", views.update, name="update"),
    path("outcome_save/", views.outcome_save, name="outcome_save"),
    path("outcome_delete/<int:outcome_id>", views.outcome_delete, name="outcome_delete"),
    path("outcome_update/<int:outcome_id>", views.outcome_update, name="outcome_update"),
]