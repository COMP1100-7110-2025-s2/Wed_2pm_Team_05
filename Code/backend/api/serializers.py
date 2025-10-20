from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

# {
#     "name": "introduction to software innovation",
#     "code": "CSE1000",
#     "level": 1,
#     "credits": 2,
#     "aim": "This course aims to introduce the fundamentals of innovation in computer science and information technology through a discipline-specific team project. Students will learn what innovation is, processes that innovators follow,
#             how innovation teams work together, how to make decisions in technology projects, how to use prototyping in the innovation process and the tools required to successfully deliver and communicate an innovation project. This course provides the foundations to further courses in computer science and information technology programs.",
#     "assessment_type": "assignment",
#     "study_area": "eait",
#     "offered_sem_1": true,
#     "offered_sem_2": true,
#     "offered_summer": false,
#     "description": "Introduction to innovation using computer science and information technology through a discipline-specific
#             team project. Students will learn what innovation is, processes that innovators follow, how innovation teams work together,
#             how to make decisions in technology projects, how to use prototyping in the innovation process
#             and the tools required to successfully deliver and communicate an innovation project.
#             This is the third offering of the course. There are no specific changes to this course
#             compared to the course description or previous offerings of this course.",
#     "assessments": [
# }