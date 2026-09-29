from datetime import date, datetime, timedelta

from books import find_book
from members import find_member
from utils import generate_id, get_non_empty_input, get_valid_date


LOAN_DAYS = 7
DATE_FORMAT = "%Y-%m-%d"


def calculate_due_date(issue_date):
    """Calculate the due date using the loan period."""
    issue_date_object = datetime.strptime(issue_date, DATE_FORMAT).date()
    due_date_object = issue_date_object + timedelta(days=LOAN_DAYS)
    return str(due_date_object)


def issue_book(data):
    """Issue a book to a member."""
    book_id = get_non_empty_input("Enter book ID: ")
    book = find_book(data, book_id)

    if book is None:
        print("Book not found.")
        return

    member_id = get_non_empty_input("Enter member ID: ")
    member = find_member(data, member_id)

    if member is None:
        print("Member not found.")
        return

    if not member["active"]:
        print("This member is inactive.")
        return

    if book["available_copies"] <= 0:
        print("No copies are currently available.")
        return

    issue_date = str(date.today())
    due_date = calculate_due_date(issue_date)
    transaction_id = generate_id(
        data["transactions"], "T", "transaction_id"
    )

    transaction = {
        "transaction_id": transaction_id,
        "book_id": book_id,
        "member_id": member_id,
        "issue_date": issue_date,
        "due_date": due_date,
        "return_date": "",
        "status": "issued",
    }

    data["transactions"].append(transaction)
    book["available_copies"] -= 1

    print("Book issued successfully.")
    print(f"Transaction ID: {transaction_id}")
    print(f"Due date: {due_date}")


def return_book(data):
    """Return a book using its active transaction."""
    transaction_id = get_non_empty_input("Enter transaction ID: ")

    transaction = None
    for item in data["transactions"]:
        if (
            item["transaction_id"].lower() == transaction_id.lower()
            and item["status"] == "issued"
        ):
            transaction = item
            break

    if transaction is None:
        print("Active transaction not found.")
        return

    book = find_book(data, transaction["book_id"])
    if book is None:
        print("Related book was not found. Return cancelled.")
        return

    return_date = str(date.today())
    transaction["return_date"] = return_date
    transaction["status"] = "returned"
    book["available_copies"] = min(
        book["available_copies"] + 1,
        book["total_copies"],
    )

    due_date = datetime.strptime(
        transaction["due_date"], DATE_FORMAT
    ).date()
    current_date = datetime.strptime(
        return_date, DATE_FORMAT
    ).date()

    print("Book returned successfully.")
    if current_date > due_date:
        late_days = (current_date - due_date).days
        print(f"Returned late by {late_days} day(s).")
    else:
        print("Book returned on time.")


def view_issued_books(data):
    """Display all currently issued books."""
    issued_transactions = [
        transaction
        for transaction in data["transactions"]
        if transaction["status"] == "issued"
    ]

    if not issued_transactions:
        print("No books are currently issued.")
        return

    print("\nCURRENTLY ISSUED BOOKS")
    print("-" * 60)

    for transaction in issued_transactions:
        print(
            f"Transaction: {transaction['transaction_id']} | "
            f"Book: {transaction['book_id']} | "
            f"Member: {transaction['member_id']} | "
            f"Issued: {transaction['issue_date']} | "
            f"Due: {transaction['due_date']}"
        )
