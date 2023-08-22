from django.urls import path
from .import views
urlpatterns = [
    path("",views.home),
    path("add",views.addemployee),
    path("display",views.display),
    # path("delete",views.delete),
    path("delete/<int:eid>",views.empdelete),
    path("update",views.update)
]