# Define the class for the course schedule
class CourseSchedule:
    def __init__(self, courses):
        self.courses = courses
        
    # Define a function to add a course to the schedule
    def add_course(self, course):
        self.courses.append(course)
        
    # Define a function to remove a course from the schedule
    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{course} not found in course schedule.")
    
    # Define a function to display the course schedule
    def display_schedule(self):
        if not self.courses:
            print("No courses currently scheduled.")
        else:
            print("Course Schedule:")
            for course in self.courses:
                print(course)
        
# Define the class for the student
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.schedule = CourseSchedule([])
        self.grades = {}
        
    # Define a function to add a course to the student's schedule
    def add_course(self, course):
        self.schedule.add_course(course)
        print(f"{course} added to {self.name}'s schedule.")
        
    # Define a function to remove a course from the student's schedule
    def remove_course(self, course):
        self.schedule.remove_course(course)
        print(f"{course} removed from {self.name}'s schedule.")
        
    # Define a function to display the student's course schedule
    def display_schedule(self):
        self.schedule.display_schedule()
        
    # Define a function to add a grade for a course
    def add_grade(self, course, grade):
        self.grades[course] = grade
        print(f"{grade} added for {course} for {self.name}.")
        
    # Define a function to display the student's grades
    def display_grades(self):
        if not self.grades:
            print("No grades to display.")
        else:
            print(f"Grades for {self.name}:")
            for course, grade in self.grades.items():
                print(f"{course}: {grade}")
        
# Create some sample courses
math_course = "Mathematics 101"
history_course = "History 101"
science_course = "Science 101"

# Create some sample students
student1 = Student("John Smith", 12345)
student2 = Student("Jane Doe", 67890)

# Have the students add courses to their schedules
student1.add_course(math_course)
student1.add_course(history_course)
student2.add_course(science_course)

# Have the students remove courses from their schedules
student1.remove_course(history_course)
student2.remove_course("Art 101") # This will result in an error message

# Have the students add grades for their courses
student1.add_grade(math_course, "A")
student2.add_grade(science_course, "B")

# Display the students' schedules and grades
student1.display_schedule()
student1.display_grades()
student2.display_schedule()
student2.display_grades()
