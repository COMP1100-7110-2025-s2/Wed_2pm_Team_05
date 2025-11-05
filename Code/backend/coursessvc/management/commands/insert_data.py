from django.core.management.base import BaseCommand
from coursessvc.models import Course, CoursePrerequisite, Assessment


class Command(BaseCommand):
    help = "Insert placeholder data for Courses, CoursePrerequisites, and Assessments."

    def handle(self, *args, **options):
        course1, _ = Course.objects.get_or_create(
            code="COMP1100",
            defaults=dict(
                name="Introduction to Software Innovation",
                level=1,
                credits=2,
                aim="""This course aims to introduce the fundamentals of innovation in computer science and information technology through a discipline-specific team project. Students will learn what innovation is, processes that innovators follow, how innovation teams work together, how to make decisions in technology projects, how to use prototyping in the innovation process and the tools required to successfully deliver and communicate an innovation project. This course provides the foundations to further courses in computer science and information technology programs.""",
                assessment_type=Course.AssessmentType.ASSIGNMENT,
                study_area=Course.StudyArea.EAIT,
                offered_sem_1=True,
                offered_sem_2=True,
                offered_summer=False,
                description="""Introduction to innovation using computer science and information technology through a discipline-specific team project. Students will learn what innovation is, processes that innovators follow, how innovation teams work together, how to make decisions in technology projects, how to use prototyping in the innovation process and the tools required to successfully deliver and communicate an innovation project.\n
                This is the third offering of the course. There are no specific changes to this course compared to the course description or previous offerings of this course.""",
            ),
        )

        Assessment.objects.get_or_create(
            course=course1,
            category="Participation/ Student contribution, Practical/ Demonstration, Presentation, Role play/ Simulation",
            task="Studio participation",
            mode="Activity/ Performance, Oral, Product/ Artefact/ Multimedia",
            grading_type=Assessment.GradingType.PASS_FAIL,
            description="""Participation in the weekly seminar and studios, including presentation and practice sessions.
This task has been designed to be challenging, authentic and complex. Whilst students may use AI and/or MT technologies, successful completion of assessment in this course will require students to critically engage in specific contexts and tasks for which artificial intelligence will provide only limited support and guidance.
A failure to reference generative AI or MT use may constitute student misconduct under the Student Code of Conduct.
To pass this assessment, students will be required to demonstrate detailed comprehension of their submission independent of AI and MT tools.""",
            hurdle=True,
            hurdle_description="""Students must attend and participate each of the weeks listed above. If there are exceptional circumstances and you are unable to attend, you must inform your team and your supervisor *before* the studio that you will be unable to attend, and provide relevant evidence to your supervisor. The course coordinator will work with you and your supervisor to determine alternative assessment to demonstrate learning outcomes.""",
        )

        Assessment.objects.get_or_create(
            course=course1,
            category="Paper/ Report/ Annotation, Product/ Design, Reflection",
            task="Business model canvas iteration 1",
            mode="Written",
            grading_type=Assessment.GradingType.PASS_FAIL,
            description="""A team report outlining the customer discovery findings from the first iteration of the process.
A short individual reflection from each student.
This task has been designed to be challenging, authentic and complex. Whilst students may use AI and/or MT technologies, successful completion of assessment in this course will require students to critically engage in specific contexts and tasks for which artificial intelligence will provide only limited support and guidance.
A failure to reference generative AI or MT use may constitute student misconduct under the Student Code of Conduct.
To pass this assessment, students will be required to demonstrate detailed comprehension of their submission independent of AI and MT tools.
Students will have one-on-one meetings with their supervisor to discuss their work throughout the semester.""",
            hurdle=True,
            hurdle_description="""This submission has both a team component, as well as a short individual self reflection. Students must achieve a Pass on both items to be eligible to Pass the course. Individual student contribution to the team component is determined by the logs in the source code repository.""",
        )

        Assessment.objects.get_or_create(
            course=course1,
            category="Paper/ Report/ Annotation, Product/ Design, Reflection",
            task="Business model canvas iteration 2",
            mode="Written",
            grading_type=Assessment.GradingType.PASS_FAIL,
            description="""A team report outlining the customer discovery findings from the second iteration of the process.
A short individual reflection from each student.
This task has been designed to be challenging, authentic and complex. Whilst students may use AI and/or MT technologies, successful completion of assessment in this course will require students to critically engage in specific contexts and tasks for which artificial intelligence will provide only limited support and guidance.
A failure to reference generative AI or MT use may constitute student misconduct under the Student Code of Conduct.
To pass this assessment, students will be required to demonstrate detailed comprehension of their submission independent of AI and MT tools.
Students will have one-on-one meetings with their supervisor to discuss their work throughout the semester.""",
            hurdle=True,
            hurdle_description="""This submission has both a team component, as well as a short individual self reflection. Students must achieve a Pass on both items to be eligible to Pass the course. Individual student contribution to the team component is determined by the logs in the source code repository.""",
        )

        Assessment.objects.get_or_create(
            course=course1,
            category="Computer Code, Paper/ Report/ Annotation, Practical/ Demonstration, Presentation, Product/ Design, Reflection",
            task="Code submission and business model canvas iteration 3",
            mode="Oral, Product/ Artefact/ Multimedia, Writtenp",
            grading_type=Assessment.GradingType.PASS_FAIL,
            description="""A team report outlining the customer discovery findings from the third iteration of the process.
An implemented conceptual prototype.
A short individual reflection from each student.
This task has been designed to be challenging, authentic and complex. Whilst students may use AI and/or MT technologies, successful completion of assessment in this course will require students to critically engage in specific contexts and tasks for which artificial intelligence will provide only limited support and guidance.
A failure to reference generative AI or MT use may constitute student misconduct under the Student Code of Conduct.
To pass this assessment, students will be required to demonstrate detailed comprehension of their submission independent of AI and MT tools.
Students will have one-on-one meetings with their supervisor to discuss their work throughout the semester.""",
            hurdle=True,
            hurdle_description="""This submission has both a team component, as well as a short individual self reflection. Students must achieve a Pass on both items to be eligible to Pass the course. Individual student contribution to the team component is determined by the logs in the source code repository."""
        )

        course2, _ = Course.objects.get_or_create(
            code="COMP1200",
            defaults=dict(
                name="Programming for Problem Solving",
                level=1,
                credits=2,
                aim="""This course aims to introduce students to computational thinking and programming using Python. Students will learn fundamental programming concepts including data types, control structures, functions, and basic algorithms. The course emphasizes problem-solving skills and the application of programming to solve real-world problems.""",
                assessment_type=Course.AssessmentType.ASSIGNMENT,
                study_area=Course.StudyArea.EAIT,
                offered_sem_1=True,
                offered_sem_2=True,
                offered_summer=True,
                description="""An introduction to programming and computational thinking using Python. Topics include variables, data types, control flow, functions, data structures, file I/O, and introductory algorithms. Students will develop problem-solving skills through practical programming exercises.""",
            ),
        )

        Assessment.objects.get_or_create(
            course=course2,
            category="Participation/ Student contribution, Practical/ Demonstration",
            task="Weekly lab exercises",
            mode="Activity/ Performance, Product/ Artefact/ Multimedia",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""Weekly hands-on programming exercises completed during lab sessions. Students will implement solutions to programming problems demonstrating understanding of course concepts.""",
            hurdle=False,
        )

        Assessment.objects.get_or_create(
            course=course2,
            category="Computer Code, Paper/ Report/ Annotation",
            task="Programming Assignment 1",
            mode="Written, Product/ Artefact/ Multimedia",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""An individual programming assignment focusing on basic Python programming concepts including variables, control structures, and functions. Students will implement a program to solve a specified problem.""",
            hurdle=False,
        )

        Assessment.objects.get_or_create(
            course=course2,
            category="Computer Code, Paper/ Report/ Annotation",
            task="Programming Assignment 2",
            mode="Written, Product/ Artefact/ Multimedia",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""An individual programming assignment focusing on data structures and file handling. Students will develop a more complex program demonstrating proficiency with Python programming.""",
            hurdle=False,
        )

        Assessment.objects.get_or_create(
            course=course2,
            category="Exam/ Test/ Quiz",
            task="Final Examination",
            mode="Written",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""A comprehensive examination covering all course material. Students will demonstrate their understanding of programming concepts through written responses and code writing.""",
            hurdle=False,
        )

        # Course 3: COMP2100
        course3, _ = Course.objects.get_or_create(
            code="COMP2100",
            defaults=dict(
                name="Software Design and Development",
                level=2,
                credits=2,
                aim="""This course aims to teach students the principles and practices of software design and development. Students will learn object-oriented programming, design patterns, software testing, version control, and collaborative development practices.""",
                assessment_type=Course.AssessmentType.ASSIGNMENT,
                study_area=Course.StudyArea.EAIT,
                offered_sem_1=True,
                offered_sem_2=True,
                offered_summer=False,
                description="""An exploration of software design and development methodologies. Topics include object-oriented design, UML diagrams, design patterns, testing strategies, Git version control, and agile development practices. Students will work on team projects to develop software applications.""",
            ),
        )

        Assessment.objects.get_or_create(
            course=course3,
            category="Computer Code, Practical/ Demonstration",
            task="Individual Programming Project",
            mode="Product/ Artefact/ Multimedia",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""An individual project where students design and implement a software application demonstrating object-oriented design principles and best practices in software development.""",
            hurdle=False,
        )

        Assessment.objects.get_or_create(
            course=course3,
            category="Computer Code, Practical/ Demonstration, Presentation",
            task="Team Software Project",
            mode="Oral, Product/ Artefact/ Multimedia",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""A collaborative team project where students work together to design, implement, and deliver a software application. Includes a presentation and demonstration of the final product.""",
            hurdle=False,
        )

        Assessment.objects.get_or_create(
            course=course3,
            category="Exam/ Test/ Quiz",
            task="Mid-semester Test",
            mode="Written",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""A test covering software design principles, object-oriented concepts, and design patterns covered in the first half of the semester.""",
            hurdle=False,
        )

        Assessment.objects.get_or_create(
            course=course3,
            category="Exam/ Test/ Quiz",
            task="Final Examination",
            mode="Written",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""A comprehensive examination covering all course material including software design, development practices, and testing methodologies.""",
            hurdle=False,
        )

        course4, _ = Course.objects.get_or_create(
            code="MATH1050",
            defaults=dict(
                name="Calculus and Linear Algebra",
                level=1,
                credits=2,
                aim="""This course aims to provide students with a foundation in calculus and linear algebra. Topics include differentiation, integration, matrices, vectors, and their applications in computer science and engineering.""",
                assessment_type=Course.AssessmentType.EXAM,
                study_area=Course.StudyArea.EAIT,
                offered_sem_1=True,
                offered_sem_2=True,
                offered_summer=True,
                description="""An introduction to calculus and linear algebra with applications. Topics include limits, derivatives, integrals, matrix operations, vector spaces, and linear transformations.""",
            ),
        )

        Assessment.objects.get_or_create(
            course=course4,
            category="Paper/ Report/ Annotation",
            task="Assignment 1",
            mode="Written",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""Written assignment covering calculus topics including differentiation and applications of derivatives.""",
            hurdle=False,
        )

        Assessment.objects.get_or_create(
            course=course4,
            category="Paper/ Report/ Annotation",
            task="Assignment 2",
            mode="Written",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""Written assignment covering integration techniques and applications of integrals.""",
            hurdle=False,
        )

        Assessment.objects.get_or_create(
            course=course4,
            category="Paper/ Report/ Annotation",
            task="Assignment 3",
            mode="Written",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""Written assignment covering linear algebra topics including matrices, vectors, and linear transformations.""",
            hurdle=False,
        )

        Assessment.objects.get_or_create(
            course=course4,
            category="Exam/ Test/ Quiz",
            task="Final Examination",
            mode="Written",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""A comprehensive examination covering all calculus and linear algebra topics from the semester.""",
            hurdle=False,
        )

        # Course 5: COMP3200
        course5, _ = Course.objects.get_or_create(
            code="COMP3200",
            defaults=dict(
                name="Database Systems",
                level=3,
                credits=2,
                aim="""This course aims to teach students the theory and practice of database systems. Topics include data modeling, SQL, database design, normalization, transactions, and database management systems.""",
                assessment_type=Course.AssessmentType.ASSIGNMENT,
                study_area=Course.StudyArea.EAIT,
                offered_sem_1=True,
                offered_sem_2=False,
                offered_summer=False,
                description="""A comprehensive study of database systems covering relational database theory, SQL programming, database design using ER diagrams, normalization, transaction management, and advanced database topics.""",
            ),
        )

        Assessment.objects.get_or_create(
            course=course5,
            category="Computer Code, Paper/ Report/ Annotation",
            task="Database Design Assignment",
            mode="Written, Product/ Artefact/ Multimedia",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""Students will design a database schema for a given scenario, including ER diagrams, normalization, and SQL implementation.""",
            hurdle=False,
        )

        Assessment.objects.get_or_create(
            course=course5,
            category="Computer Code, Practical/ Demonstration",
            task="SQL Programming Project",
            mode="Product/ Artefact/ Multimedia",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""A practical project where students implement complex SQL queries and database operations for a real-world application.""",
            hurdle=False,
        )

        Assessment.objects.get_or_create(
            course=course5,
            category="Exam/ Test/ Quiz",
            task="Final Examination",
            mode="Written",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""A comprehensive examination covering database theory, SQL, design principles, and database management concepts.""",
            hurdle=False,
        )

        CoursePrerequisite.objects.get_or_create(
            course=course3,
            prereq=course2,
        )

        CoursePrerequisite.objects.get_or_create(
            course=course5,
            prereq=course2,
        )

        self.stdout.write(self.style.SUCCESS('Successfully inserted course data'))
