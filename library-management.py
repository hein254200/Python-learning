

def view():
        print(f"\n{"Book list ":^35}")
        print(f"{"______________________":^35}")
        print(f"{"Id":<10}{"Title":<10}{"Author":<10}{"Page":<5}")
        for book in books:
            print(f"{book["id"]:<10}{book["title"]:<10}{book["author"]:<10}{book["pages"]:<5}")

def find():
    book_title=input("Enter book name you want to search:")
    for book in books:
        if book_title==book["title"]:
            print(f"Book id={book["id"]}\nBook title={book['title']}\nAuthor={book["author"]} ")
            return
    print("the book doesn't exist!")

def add():
    global book_count
    new_id = f"00{book_count}"
    book_count+=1
    new_title=input("Enter new book title:")
    new_author = input("Enter book Author:")
    new_pages = int(input("Enter book Pages:"))
    new_book= {
        "title":new_title,
        "author":new_author,
        "id":new_id,
        "pages":new_pages
        }
    books.append(new_book)
    print("Book added successfully!")

def delete():
    view()
    del_book= input("Enter book id you want to delete!:")
    for book in books:
        if del_book==book["id"]:
            books.remove(book)
            print("Book deleted successfully!")
            return
    print("Invalid id! Please try again!")

def main():
    print("\nWelcome to my library!!!")
    print("1:view books ")
    print("2:find books ")
    print("3:add books ")
    print("4:delete books ")
    print("1:exit ")

    option={
         1:view,
         2:find,
         3:add,
         4:delete
            }
    while True:
        op=int(input("\nchoose option(1~5):"))
        if 1<=op<=5:
            if op ==5:
                  print("Thank you for using our library!!")
                  break
            option[op]()
        else:
             print("invalid choose")

books=[{"title":"python",
        "author":"hein",
        "id":"001",
        "pages":100
        },
        {
        "title":"C++",
        "author":"min",
        "id":"002",
        "pages":150
        },
        {
        "title":"java",
        "author":"htet",
        "id":"003",
        "pages":200
        }
]
book_count=len(books)+1
main()

