user_name = "hein"
user_id = 1234
name = input("what is your name?")
id = int (input("what is your id?"))
if name == user_name and id == user_id:
    print("login successful!")
    print(f"welcome {name} your id is {id}.")
else:
    print("wrong name or id!")