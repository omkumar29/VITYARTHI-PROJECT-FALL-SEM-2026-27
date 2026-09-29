def search_books(data):
    """Search books by ID, title, author, or category."""
    keyword = input("Enter book search text: ").strip().lower()

    if not keyword:
        print("Search text cannot be empty.")
        return

    results = []
    for book in data["books"]:
        searchable_text = [
            book["book_id"],
            book["title"],
            book["author"],
            book["category"],
        ]

        if any(keyword in str(value).lower() for value in searchable_text):
            results.append(book)

    if not results:
        print("No matching books found.")
        return

    print("\nSEARCH RESULTS")
    print("-" * 60)
    for book in results:
        print(
            f"{book['book_id']} | {book['title']} | "
            f"{book['author']} | {book['category']} | "
            f"Available: {book['available_copies']}/{book['total_copies']}"
        )


def search_members(data):
    """Search members by ID, name, or course."""
    keyword = input("Enter member search text: ").strip().lower()

    if not keyword:
        print("Search text cannot be empty.")
        return

    results = []
    for member in data["members"]:
        searchable_text = [
            member["member_id"],
            member["name"],
            member["course"],
            member["semester"],
        ]

        if any(keyword in str(value).lower() for value in searchable_text):
            results.append(member)

    if not results:
        print("No matching members found.")
        return

    print("\nMEMBER SEARCH RESULTS")
    print("-" * 60)
    for member in results:
        status = "Active" if member["active"] else "Inactive"
        print(
            f"{member['member_id']} | {member['name']} | "
            f"{member['course']} | {status}"
        )
