from datetime import date, datetime


DATE_FORMAT = "%Y-%m-%d"


def show_library_summary(data):
    """Display the main library statistics."""
    books = data["books"]
    members = data["members"]
    transactions = data["transactions"]

    total_titles = len(books)
    total_copies = sum(book["total_copies"] for book in books)
    available_copies = sum(book["available_copies"] for book in books)
    issued_copies = total_copies - available_copies
    total_members = len(members)
    active_members = sum(1 for member in members if member["active"])

    print("\nLIBRARY SUMMARY")
    print("-" * 60)
    print(f"Total book titles: {total_titles}")
    print(f"Total book copies: {total_copies}")
    print(f"Available copies: {available_copies}")
    print(f"Issued copies: {issued_copies}")
    print(f"Total members: {total_members}")
    print(f"Active members: {active_members}")
    print(f"Total transactions: {len(transactions)}")


def show_overdue_books(data):
    """Display books that are still issued after their due date."""
    today = date.today()
    overdue_transactions = []

    for transaction in data["transactions"]:
        if transaction["status"] != "issued":
            continue

        due_date = datetime.strptime(
            transaction["due_date"], DATE_FORMAT
        ).date()

        if due_date < today:
            overdue_transactions.append(transaction)

    if not overdue_transactions:
        print("No overdue books.")
        return

    print("\nOVERDUE BOOKS")
    print("-" * 60)

    for transaction in overdue_transactions:
        print(
            f"Transaction: {transaction['transaction_id']} | "
            f"Book: {transaction['book_id']} | "
            f"Member: {transaction['member_id']} | "
            f"Due: {transaction['due_date']}"
        )


def show_category_report(data):
    """Display the number of book titles in each category."""
    category_counts = {}

    for book in data["books"]:
        category = book["category"]
        category_counts[category] = category_counts.get(category, 0) + 1

    if not category_counts:
        print("No book data available.")
        return

    print("\nCATEGORY REPORT")
    print("-" * 60)
    for category, count in sorted(category_counts.items()):
        print(f"{category}: {count} title(s)")
