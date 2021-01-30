n = int(input())
students = {}
for _ in range(n):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []
    students[name].append(grade)

filtered_students = {el: sum(students[el]) / len(students[el]) for el in students if
                     sum(students[el]) / len(students[el]) >= 4.50}

for student, av_grade in sorted(filtered_students.items(), key=lambda x: x[1], reverse=True):
    print(f"{student} -> {av_grade:.2f}")
