from django.urls import path
from .views import GoToAdminView

app_name = "demo"

urlpatterns = [
    path("go-to-admin/", GoToAdminView.as_view(), name="go-to-admin")
]