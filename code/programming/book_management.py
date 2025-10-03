"""

* OOPS - Classes: Book, Member, Library. Members can borrow/return books. Track available vs borrowed books.

"""
import os

# Ensure output folder exists
output_folder = "./code/output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


class Book:
  """
  A class representing a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        is_borrowed (bool): Status indicating if the book is borrowed.
    """
  def __init__(self, title, author):
      """
      Initializes a new Book instance
        """
      self.title = title
      self.author = author
      self.is_borrowed = False




class Member:
   
   """
    Represents a library member.

    Attributes:
        name (str): Name of the member.
        borrowed_books (list): List of borrowed Book objects.
    """
     
   def __init__(self, name):
        """
          Initializes a new Member instance.
          """
        self.name = name
        self.borrowed_books = []
   def borrow_book(self, book):
        """
        Borrows a book if it's available.
        
        Args:
            book (Book): The book to borrow.
            library (Library): The library instance.
         """
        if library.lend_book(book):
            self.borrowed_books.append(book)
            self._write_output(f"{self.name} borrowed '{book.title}'.")
        else:
            self._write_output(f"'{book.title}' is not available to borrow.")   
   def return_book(self, book, library):
        """
        Return a borrowed book to the library.

        Args:
            book (Book): Book to return.
            library (Library): Library object to return to.
        """
        if book in self.borrowed_books:
            library.receive_book(book)
            self.borrowed_books.remove(book)
            self._write_output(f"{self.name} returned '{book.title}'.")
        else:
            self._write_output(f"{self.name} cannot return '{book.title}' (not borrowed).")

   def _write_output(self, message):
        """Writes messages to the output file."""
        with open(f"{output_folder}/library_output.txt", "a") as file:
            file.write(message + "\n")       

class Library:
      """
    Represents a library containing books.

    Attributes:
        books (list): List of Book objects in the library.
    """
      def __init__(self):
        """Initialize a new Library object."""
        self.books = []

      def add_book(self, book):
        """Add a new book to the library."""
        self.books.append(book)
        self._write_output(f"Added book '{book.title}' by {book.author} to library.")

      def lend_book(self, book):
        """
        Lend a book if available.

        Args:
            book (Book): Book to lend.

        Returns:
            bool: True if lending successful, False otherwise.
        """
        if book in self.books and not book.is_borrowed:
            book.is_borrowed = True
            return True
        return False

      def receive_book(self, book):
        """Receive a returned book and mark it as available."""
        if book in self.books:
            book.is_borrowed = False

      def available_books(self):
        """Return a list of books currently available."""
        available = [book for book in self.books if not book.is_borrowed]
        self._write_output("Available books: " + ", ".join([b.title for b in available]))
        return available

      def borrowed_books(self):
        """Return a list of books currently borrowed."""
        borrowed = [book for book in self.books if book.is_borrowed]
        self._write_output("Borrowed books: " + ", ".join([b.title for b in borrowed]))
        return borrowed

      def _write_output(self, message):
        """Writes messages to the output file."""
        with open(f"{output_folder}/library_output.txt", "a") as file:
            file.write(message + "\n")


library = Library()
# creating books
book1 = Book("1984", "george orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

# adding books to library
library.add_book(book1)
library.add_book(book2)

# adding member
member1= Member("yash")
member2= Member("shiva")


member1.borrow_book(book1)
member2.borrow_book(book1)  # Should show not available
member2.borrow_book(book2)

member1.return_book(book1,library)
member2.borrow_book(book1)  # Now available

library.available_books()
library.borrowed_books()
