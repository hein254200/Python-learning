books = ["python book","C language","IT passport","FE book"]
running = True#to loop the program

print("------------------")
print("Welcom to my book collection!")
print("1. view Books")
print("2. Find Books")
print("3. Add Books")
print("4. Delete Books")
print("5. Exit")
print("------------------")


while running:
    op = int(input("\nChoise operation:"))
    #to view books
    if op==1:
        print("***Book List***")
        for index,book in enumerate(books):
            print(f"{index+1}.{book}")
        print("   ******   ")


    #to find books
    elif op == 2:
        book_name = input("Enter the name of book you want to search:")
        found =False
        for book in books:
            if book_name==book:
                print(f"{book_name} found at number {books.index(book_name)+1}")
                found = True
                break
        if not found:
            print("the book does not exist!")
                    
    #to add book
    elif op == 3:
        new_book =input("Enter new book:")
        books.append(new_book)
        print("New book is added successfully.")

    #to delete
    elif op == 4:
        print("***Book List***")
        for index,book in enumerate(books):
            print(f"{index+1}.{book}")
        print("   ******   ")
        #user အမြင်မှာနံပါတ်က ၁ ကနေစတာဖြစ်လို့index အမှန်ဖြစ်အောင် ၁ နှုတ်ပေးလိုက်တယ်
        index = int(input("Enter the number of book you want to delete:"))-1
        if 0<=index<len(books):#0~3
            books.pop(index)
            print("book is deleted successfully.")
        else:
            print("Invalid number!")

    elif op == 5:
        running = False
        print("Thanks,Goodbye!")
    else:
        print("Invalid choice! Please try again.")
