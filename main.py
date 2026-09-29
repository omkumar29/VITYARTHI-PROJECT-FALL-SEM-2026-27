import json
from pathlib import Path

import books
import issue_return
import members
import reports
import search
from utils import print_line


DATA_FILE = Path(__file__).resolve().parent / "data" / "library_data.json"


def create_empty_data_file():
    """Create the data folder and JSON file when needed."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not DATA_FILE.exists():
        save_data({
            "books": [],
            "members": [],
            "transactions": [],
        })


def load_data():
    """Load data from JSON and handle file problems safely."""
    create_empty_data_file()

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary.")

        data.setdefault("books", [])
        data.setdefault("members", [])
        data.setdefault("transactions", [])

        return data

    except (json.JSONDecodeError, OSError, ValueError):
        print("Data file is missing or invalid.")
        print("A new empty data set will be used.")

        return {
            "books": [],
            "members": [],
            "transactions": [],
        }


def save_data(data):
    """Save current data to JSON."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def book_menu(data):
    """Show the book management submenu."""
    while True:
        print("\nBOOK MANAGEMENT")
        print_line()
        print("1. Add Book")
        print("2. View All Books")
        print("3. View Available Books")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            books.add_book(data)
            save_data(data)
        elif choice == "2":
            books.view_books(data)
        elif choice == "3":
            books.view_books(data, only_available=True)
        elif choice == "4":
            books.update_book(data)
            save_data(data)
        elif choice == "5":
            books.delete_book(data)
            save_data(data)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


def member_menu(data):
    """Show the member management submenu."""
    while True:
        print("\nMEMBER MANAGEMENT")
        print_line()
        print("1. Add Member")
        print("2. View All Members")
        print("3. View Individual Member")
        print("4. Update Member")
        print("5. Delete Member")
        print("6. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            members.add_member(data)
            save_data(data)
        elif choice == "2":
            members.view_members(data)
        elif choice == "3":
            members.view_individual_member(data)
        elif choice == "4":
            members.update_member(data)
            save_data(data)
        elif choice == "5":
            members.delete_member(data)
            save_data(data)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


def issue_return_menu(data):
    """Show the issue and return submenu."""
    while True:
        print("\nISSUE / RETURN BOOK")
        print_line()
        print("1. Issue Book")
        print("2. Return Book")
        print("3. View Issued Books")
        print("4. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            issue_return.issue_book(data)
            save_data(data)
        elif choice == "2":
            issue_return.return_book(data)
            save_data(data)
        elif choice == "3":
            issue_return.view_issued_books(data)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


def search_menu(data):
    """Show the search submenu."""
    while True:
        print("\nSEARCH")
        print_line()
        print("1. Search Books")
        print("2. Search Members")
        print("3. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            search.search_books(data)
        elif choice == "2":
            search.search_members(data)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


def reports_menu(data):
    """Show the reports submenu."""
    while True:
        print("\nLIBRARY REPORTS")
        print_line()
        print("1. Library Summary")
        print("2. Overdue Books")
        print("3. Category Report")
        print("4. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            reports.show_library_summary(data)
        elif choice == "2":
            reports.show_overdue_books(data)
        elif choice == "3":
            reports.show_category_report(data)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


def main_menu():
    """Run the main application menu."""
    data = load_data()

    while True:
        print("\n" + "=" * 60)
        print("LIBRARY MANAGEMENT SYSTEM")
        print("=" * 60)
        print("1. Book Management")
        print("2. Member Management")
        print("3. Issue / Return Book")
        print("4. Search")
        print("5. Library Reports")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            book_menu(data)
        elif choice == "2":
            member_menu(data)
        elif choice == "3":
            issue_return_menu(data)
        elif choice == "4":
            search_menu(data)
        elif choice == "5":
            reports_menu(data)
        elif choice == "6":
            save_data(data)
            print("Thank you for using the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
