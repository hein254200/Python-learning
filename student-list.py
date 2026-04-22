students=[
    {
        'id':'001',
        'name':'hein',
        'region':'myanmar'

    },{
        'id':'002',
        'name':'aniru',
        'region':'nepal'
    },{
        'id':'003',
        'name':'funn',
        'region':'vietnam'
    }
]
running = True

print("------------------")
print("Welcom !")
print("1. view students list")
print("2. Find student")
print("3. Add student")
print("4. Delete student")
print("5. Exit")
print("------------------")

#to view  function
def view_students():
    print("\n***student List***")
    print(" ID \t name \t region ")
    print("------------------------")
    for student in students:
        print(f"{student['id']} \t {student['name']} \t {student['region']}")
    print("\t  ******   ")

#to find function
def find_students():
    student_id = input("Enter id of student you want to search:")
    found =False
    for student in students:
        if student_id==student['id']:
            print(f"Student id = {student['id'] }")
            print(f"Student name = {student['name'] }")
            print(f"Region = {student['region'] }")
            found = True
            break
    if not found:
        print(f"id-{student_id} does not exist!")

#to add function
def add_students():
    if len(students)<=0:
        new_id='001'
    else:
        #find the last item of data.
        #str နဲ့ဝင်လာတဲ့ ID ကို slicing လုပ်။(00=str,the last one is int.)
        last_student=students[-1] #list data ရဲ့နောက်ဆုံး index ကိုရှာ
        f_part= last_student['id'][:2] #to slice for first 2 char.
        l_part = int(last_student['id'][2:])#chane the last char to int.
        new_part = l_part+1# 00+(_+1)
        new_id = f_part + str(new_part)#00_
    new_student =input("Enter new student name:")
    new_region=input("Enter region:")
    students.append({'id':new_id,'name':new_student,'region':new_region})
        
    print("Student is added successfully.")

#to delete  function
def delete_students():
        view_students()
        d_id = input("Enter ID of student you want to delete:")
        found = False
        for i in range(len(students)):
            if d_id == students[i]['id']:
                students.pop(i)
                print("deleted successful!")
                found = True
                break
        if not found:
            print("Invalid id")

            

while running:
    op = int(input("\nChoise operation:"))
    
    if op==1:
        view_students()

    elif op == 2:
        find_students()
                    
    elif op == 3:
        add_students()

    elif op == 4:
        delete_students()

    elif op == 5:
        running = False
        print("Thanks,Goodbye!")
    else:
        print("Invalid choice! Please try again.")
