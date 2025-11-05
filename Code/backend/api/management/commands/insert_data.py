
from django.core.management.base import BaseCommand
from api.models import Course, CoursePrerequisite, Assessment


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
            code="COMP2100",
            defaults=dict(
                name="Data Structures and Algorithms",
                level=2,
                credits=6,
                aim="""This course provides students with a comprehensive understanding of fundamental data structures and algorithms essential for efficient software development. Students will learn to analyze algorithm complexity, implement various data structures, and apply algorithmic techniques to solve computational problems.""",
                assessment_type=Course.AssessmentType.EXAM,
                study_area=Course.StudyArea.EAIT,
                offered_sem_1=True,
                offered_sem_2=True,
                offered_summer=False,
                description="""Topics include arrays, linked lists, stacks, queues, trees, graphs, sorting algorithms, searching algorithms, and hash tables. Students will develop skills in algorithm analysis and design patterns.""",
            ),
        )

        Assessment.objects.get_or_create(
            course=course2,
            category="Examination",
            task="Final Exam",
            mode="Written",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""A comprehensive examination covering all topics taught in the course.""",
            hurdle=False,
        )

        course3, _ = Course.objects.get_or_create(
            code="MATH1115",
            defaults=dict(
                name="Advanced Mathematics and Applications",
                level=1,
                credits=6,
                aim="""This course introduces students to advanced mathematical concepts including calculus, linear algebra, and discrete mathematics. Students will develop strong mathematical reasoning skills applicable to science and engineering.""",
                assessment_type=Course.AssessmentType.EXAM,
                study_area=Course.StudyArea.EAIT,
                offered_sem_1=True,
                offered_sem_2=False,
                offered_summer=True,
                description="""Coverage includes differential and integral calculus, matrix operations, vector spaces, probability theory, and mathematical proofs.""",
            ),
        )

        Assessment.objects.get_or_create(
            course=course3,
            category="Examination, Assignment",
            task="Mid-semester Test",
            mode="Written",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""A written test covering the first half of course material.""",
            hurdle=False,
        )

        course4, _ = Course.objects.get_or_create(
            code="ENGN3200",
            defaults=dict(
                name="Systems Engineering Design",
                level=3,
                credits=6,
                aim="""This course develops students' ability to design and analyze complex engineering systems. Students will learn systems thinking, requirements engineering, and project management methodologies.""",
                assessment_type=Course.AssessmentType.ASSIGNMENT,
                study_area=Course.StudyArea.EAIT,
                offered_sem_1=False,
                offered_sem_2=True,
                offered_summer=False,
                description="""Topics include systems lifecycle, requirements analysis, design verification, risk management, and systems integration. Students will complete a major design project.""",
            ),
        )

        Assessment.objects.get_or_create(
            course=course4,
            category="Product/ Design, Presentation",
            task="Design Project",
            mode="Product/ Artefact/ Multimedia, Oral",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""A comprehensive systems design project with oral presentation.""",
            hurdle=False,
        )

        course5, _ = Course.objects.get_or_create(
            code="COMP4500",
            defaults=dict(
                name="Advanced Algorithms and Complexity",
                level=4,
                credits=6,
                aim="""This advanced course explores computational complexity theory, advanced algorithmic techniques, and NP-completeness. Students will develop expertise in analyzing and designing algorithms for complex computational problems.""",
                assessment_type=Course.AssessmentType.ASSIGNMENT,
                study_area=Course.StudyArea.EAIT,
                offered_sem_1=True,
                offered_sem_2=False,
                offered_summer=False,
                description="""Topics include dynamic programming, greedy algorithms, graph algorithms, computational complexity classes, approximation algorithms, and randomized algorithms.""",
            ),
        )

        Assessment.objects.get_or_create(
            course=course5,
            category="Paper/ Report/ Annotation, Computer Code",
            task="Algorithm Analysis Report",
            mode="Written",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""A detailed analysis and implementation of advanced algorithms.""",
            hurdle=False,
        )

        course6, _ = Course.objects.get_or_create(
            code="STAT2001",
            defaults=dict(
                name="Statistical Methods and Analysis",
                level=2,
                credits=6,
                aim="""This course provides a foundation in statistical methods used in data analysis and scientific research. Students will learn statistical inference, hypothesis testing, and data visualization techniques.""",
                assessment_type=Course.AssessmentType.ASSIGNMENT,
                study_area=Course.StudyArea.EAIT,
                offered_sem_1=True,
                offered_sem_2=True,
                offered_summer=True,
                description="""Coverage includes descriptive statistics, probability distributions, confidence intervals, regression analysis, ANOVA, and experimental design.""",
            ),
        )

        Assessment.objects.get_or_create(
            course=course6,
            category="Paper/ Report/ Annotation, Practical/ Demonstration",
            task="Statistical Analysis Project",
            mode="Written, Product/ Artefact/ Multimedia",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""A practical data analysis project using real-world datasets.""",
            hurdle=False,
        )

        course7, _ = Course.objects.get_or_create(
            code="COMP3310",
            defaults=dict(
                name="Web Development and Cloud Computing",
                level=3,
                credits=6,
                aim="""This course teaches modern web development practices and cloud computing technologies. Students will learn to build scalable web applications using contemporary frameworks and cloud services.""",
                assessment_type=Course.AssessmentType.ASSIGNMENT,
                study_area=Course.StudyArea.EAIT,
                offered_sem_1=True,
                offered_sem_2=True,
                offered_summer=False,
                description="""Topics include front-end frameworks, RESTful APIs, database design, cloud deployment, containerization, and DevOps practices.""",
            ),
        )

        Assessment.objects.get_or_create(
            course=course7,
            category="Computer Code, Product/ Design, Practical/ Demonstration",
            task="Web Application Development",
            mode="Product/ Artefact/ Multimedia",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""Development and deployment of a full-stack web application on a cloud platform.""",
            hurdle=False,
        )

        course8, _ = Course.objects.get_or_create(
            code="ENGN2200",
            defaults=dict(
                name="Digital Electronics and Microcontrollers",
                level=2,
                credits=6,
                aim="""This course introduces digital electronics fundamentals and microcontroller programming. Students will learn to design digital circuits and program embedded systems for real-world applications.""",
                assessment_type=Course.AssessmentType.ASSIGNMENT,
                study_area=Course.StudyArea.EAIT,
                offered_sem_1=False,
                offered_sem_2=True,
                offered_summer=False,
                description="""Topics include Boolean algebra, combinational and sequential logic, microcontroller architecture, embedded C programming, and interfacing with sensors and actuators.""",
            ),
        )

        Assessment.objects.get_or_create(
            course=course8,
            category="Practical/ Demonstration, Computer Code",
            task="Embedded Systems Project",
            mode="Activity/ Performance, Product/ Artefact/ Multimedia",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""Design and implementation of an embedded system using microcontrollers.""",
            hurdle=False,
        )

        course9, _ = Course.objects.get_or_create(
            code="COMP3500",
            defaults=dict(
                name="Machine Learning and Artificial Intelligence",
                level=3,
                credits=6,
                aim="""This course provides a comprehensive introduction to machine learning and AI techniques. Students will learn supervised and unsupervised learning algorithms, neural networks, and their applications in solving real-world problems.""",
                assessment_type=Course.AssessmentType.ASSIGNMENT,
                study_area=Course.StudyArea.EAIT,
                offered_sem_1=True,
                offered_sem_2=True,
                offered_summer=False,
                description="""Topics include regression, classification, clustering, deep learning, convolutional neural networks, natural language processing, and ethical considerations in AI.""",
            ),
        )

        Assessment.objects.get_or_create(
            course=course9,
            category="Computer Code, Paper/ Report/ Annotation",
            task="Machine Learning Project",
            mode="Written, Product/ Artefact/ Multimedia",
            grading_type=Assessment.GradingType.PERCENTAGE,
            description="""Implementation and evaluation of machine learning models on a real-world dataset with comprehensive analysis report.""",
            hurdle=False,
        )