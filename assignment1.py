class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def show(self):
        print("Title:", self.name)
        print("Author:", self.author)


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def show(self):
        print("Member:", self.name)
        print("ID:", self.member_id)


class Library:
    def add_book(self, book):
        print(book.name, "added to library.")

    def add_member(self, member):
        print(member.name, "added as a member.")

    def issue_book(self, member, book):
        print(book.name, "issued to", member.name)

    def submit_book(self, member, book):
        print(member.name, "submitted", book.name)


# Creating Objects
book1 = Book("Data Structures", "Ananya Pandey")
member1 = Member("Tanya", 201)
library = Library()

# Calling Methods
library.add_book(book1)
library.add_member(member1)
library.issue_book(member1, book1)
library.submit_book(member1, book1)

'''Data Structures added to library.
Tanya added as a member.
Data Structures issued to Tanya
Tanya submitted Data Structures'''