def delete_students():
        view_students()
    
        d_id = int(input("Enter ID of student you want to delete:"))
        for student in students:
            if d_id == student['id']:
                students.pop({'name':student['name'],'id':student['id'],'region':student['region']})
                print("deleted successful!")