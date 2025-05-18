class Book:
    total_books = 0

    @classmethod
    def increment_total_books(cls):
        cls.total_books += 1
    



Book.increment_total_books()
Book.increment_total_books()
Book.increment_total_books()

print(f"Total Books: {Book.total_books}")
