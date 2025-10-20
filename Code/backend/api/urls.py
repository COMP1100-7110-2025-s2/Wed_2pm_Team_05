from django.urls import path
import api.views

urlpatterns = [
    path("courses/", api.views.CourseList.as_view(), name="course-list"),
]