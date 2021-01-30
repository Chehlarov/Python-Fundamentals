class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)
           # Class.__students_count += 1

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)

    def __repr__(self):
        students_string = ", ".join(self.students)
        return f"The students in {self.name}: " \
               f"{students_string}. Average grade: " \
               f"{self.get_average_grade():.2f}"
