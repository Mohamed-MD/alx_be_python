class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def check_out(self):
        self.__is_checked_out = True

    def return_book(self):
        self.__is_checked_out = False

    def is_available(self):
        return not self.__is_checked_out

class Library:
    def __init__(self):
        # قائمة تحتوي على كل الكتب في المكتبة
        self._books = []

    def add_book(self, book):
        """إضافة كتاب جديد إلى المكتبة"""
        self._books.append(book)

    def check_out_book(self, title):
        """استعارة كتاب بناءً على العنوان"""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"{title} has been checked out.")
                return
        print(f"{title} is not available.")

    def return_book(self, title):
        """إرجاع كتاب بناءً على العنوان"""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"{title} has been returned.")
                return
        print(f"{title} was not checked out.")

    def list_available_books(self):
        """عرض كل الكتب المتاحة حالياً"""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")


