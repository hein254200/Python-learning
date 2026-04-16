books = ["python book","C language","IT passport","FE book"]#
running = True#to loop the program

print("------------------")
print("Welcom to my book collection!")
print("1. view Books")
print("2. Find Books")
print("3. Add Books")
print("4. Delete Books")
print("5. Exit")
print("------------------")

#to view books function
def view_books():
    print("***Book List***")
    for index,book in enumerate(books):
            print(f"{index+1}.{book}")
    print("   ******   ")

#to find books function
def find_books():
    book_name = input("Enter the name of book you want to search:")
    found =False
    for book in books:
        if book_name==book:
            print(f"{book_name} found at number {books.index(book_name)+1}")
            found = True
            break
    if not found:
        print("the book does not exist!")

#to add book function
def add_books():
    new_book =input("Enter new book:")
    books.append(new_book)
    print("New book is added successfully.")

#to delete books function
def delete_books():
        view_books()
        #user အမြင်မှာနံပါတ်က ၁ ကနေစတာဖြစ်လို့index အမှန်ဖြစ်အောင် ၁ နှုတ်ပေးလိုက်တယ်
        index = int(input("Enter the number of book you want to delete:"))-1
        if 0<=index<len(books):#0~3
            books.pop(index)
            print("book is deleted successfully.")
        else:
            print("Invalid number!")

while running:
    op = int(input("\nChoise operation:"))
    
    if op==1:
        view_books()

    elif op == 2:
        find_books()
                    
    elif op == 3:
        add_books()

    elif op == 4:
        delete_books()

    elif op == 5:
        running = False
        print("Thanks,Goodbye!")
    else:
        print("Invalid choice! Please try again.")
