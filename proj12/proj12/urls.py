from django.contrib import admin
from django.urls import path
from api.views import StudentAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',StudentAPI.as_view()),
    path('studentapi/<int:pk>',StudentAPI.as_view()),
]
