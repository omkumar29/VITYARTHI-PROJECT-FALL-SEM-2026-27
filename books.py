from utils import (
    find_record,
    generate_id,
    get_non_empty_input,
    get_optional_text,
    get_positive_integer,
)


def find_book(data, book_id):
    """Find a book by its ID."""
    return find_record(data["books"], "book_id", book_id)


def add_book(data):
    """Add a new book."""
    books = data["books"]
    book_id = generate_id(books, "B", "book_id")

    title = get_non_empty_input("Enter book title: ")
    author = get_non_empty_input("Enter author name: ")
    category = get_non_empty_input("Enter category: ")
    publisher = get_non_empty_input("Enter publisher: ")
    year = get_positive_integer("Enter publication year: ")
    total_copies = get_positive_integer("Enter total copies: ")

    book = {
        "book_id": book_id,
        "title": title,
        "author": author,
        "category": category,
        "publisher": publisher,
        "year": year,
        "total_copies": total_copies,
        "available_copies": total_copies,
    }

    books.append(book)
    print(f"Book added successfully. Book ID: {book_id}")


def display_book(book):
    """Display one book in a readable format."""
    print(
        f"{book['book_id']} | {book['title']} | "
        f"{book['author']} | {book['category']} | "
        f"Available: {book['available_copies']}/{book['total_copies']}"
    )


def view_books(data, only_available=False):
    """View all books or only available books."""
    books = data["books"]
    selected_books = [
        book for book in books
        if not only_available or book["available_copies"] > 0
    ]

    if not selected_books:
        print("No books found.")
        return

    print("\nBOOK LIST")
    print("-" * 60)
    for book in selected_books:
        display_book(book)


def update_book(data):
    """Update information about a book."""
    book_id = get_non_empty_input("Enter book ID to update: ")
    book = find_book(data, book_id)

    if book is None:
        print("Book not found.")
        return

    print("Press Enter to keep the old value.")
    book["title"] = get_optional_text("Title", book["title"])
    book["author"] = get_optional_text("Author", book["author"])
    book["category"] = get_optional_text("Category", book["category"])
    book["publisher"] = get_optional_text("Publisher", book["publisher"])

    year_text = input(f"Year [{book['year']}]: ").strip()
    if year_text:
        try:
            year = int(year_text)
            if year > 0:
                book["year"] = year
            else:
                print("Invalid year. Old year kept.")
        except ValueError:
            print("Invalid year. Old year kept.")

    copies_text = input(
        f"Total copies [{book['total_copies']}]: "
    ).strip()

    if copies_text:
        try:
            new_total = int(copies_text)
            issued_copies = book["total_copies"] - book["available_copies"]

            if new_total >= issued_copies and new_total > 0:
                book["total_copies"] = new_total
                book["available_copies"] = new_total - issued_copies
            else:
                print("Total copies cannot be less than issued copies.")
        except ValueError:
            print("Invalid number. Old copy count kept.")

    print("Book updated successfully.")


def delete_book(data):
    """Delete a book if it has no active issued copies."""
    book_id = get_non_empty_input("Enter book ID to delete: ")
    book = find_book(data, book_id)

    if book is None:
        print("Book not found.")
        return

    if book["available_copies"] != book["total_copies"]:
        print("Cannot delete a book with active issued copies.")
        return

    data["books"].remove(book)
    print("Book deleted successfully.")


def book_exists(data, book_id):
    """Return True if a book exists."""
    return find_book(data, book_id) is not None


def check_book_availability(data, book_id):
    """Return True if a book has an available copy."""
    book = find_book(data, book_id)
    return book is not None and book["available_copies"] > 0
