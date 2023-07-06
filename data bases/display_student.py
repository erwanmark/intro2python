from student import Student

users = Student.select()
#use forloop to display
for user in users:
    print(user.name, user.gender, user.studentcode, user.phonenumber, user.age)
