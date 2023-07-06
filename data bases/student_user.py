from student import Student

try:
    jina = input("Enter Name\n")
    jinsia = input("Enter gender\n")
    kijulisho = input ("Enter Studentcode\n")
    simu = input ("Enter Phonenumber\n")
    miaka = input ("Enter Age\n")


    Student.create(name =jina, gender=jinsia, kijulisho=Studentcode, simu=phonenumber, miaka=Age)
    print("User Created Succesfully")

except:
        print("Filed to create user")