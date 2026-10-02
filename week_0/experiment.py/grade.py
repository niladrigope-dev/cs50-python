
students = {}
while True:

    try:
        name = input("Name:")
        if name == "done":
            break
        score = int(input("Score: "))
        if not 0 <= score <= 100:
            raise ValueError
        students[name] = score


        
      
        
    except ValueError:
        print("Invalid Value")  







avg = sum(students.values())
average = avg / len(students)

highest_no = max(students.items() , key=lambda item:item[1])
lowest = min(students.items(), key=lambda item: item[1])
no_of_students = len(students)
gstudent =[]

for student in students:
    if students[student] >= 90:
         gstudent.append(student)
serial = sorted(students.items(),key=lambda student:student[1],reverse=True)      
print("Average:", average)
print("Highest:", highest_no)
print("Lowest:", lowest)
print("Number of students:", no_of_students)
print("Students scoring 90 or above:", gstudent)
print("Sorted students:", serial)