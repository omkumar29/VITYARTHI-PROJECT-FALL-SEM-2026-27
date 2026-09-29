from datetime import date

from utils import (
    find_record,
    generate_id,
    get_non_empty_input,
    get_optional_text,
)


def find_member(data, member_id):
    """Find a member by ID."""
    return find_record(data["members"], "member_id", member_id)


def add_member(data):
    """Add a new library member."""
    members = data["members"]
    member_id = generate_id(members, "M", "member_id")

    name = get_non_empty_input("Enter member name: ")
    course = get_non_empty_input("Enter course/branch: ")
    semester = get_non_empty_input("Enter semester: ")
    email = input("Enter email (optional): ").strip()

    member = {
        "member_id": member_id,
        "name": name,
        "course": course,
        "semester": semester,
        "email": email,
        "date_joined": str(date.today()),
        "active": True,
    }

    members.append(member)
    print(f"Member added successfully. Member ID: {member_id}")


def display_member(member):
    """Display one member."""
    status = "Active" if member["active"] else "Inactive"
    print(
        f"{member['member_id']} | {member['name']} | "
        f"{member['course']} | Semester: {member['semester']} | "
        f"Status: {status}"
    )


def view_members(data):
    """View all members."""
    if not data["members"]:
        print("No members found.")
        return

    print("\nMEMBER LIST")
    print("-" * 60)
    for member in data["members"]:
        display_member(member)


def view_individual_member(data):
    """View one member."""
    member_id = get_non_empty_input("Enter member ID: ")
    member = find_member(data, member_id)

    if member is None:
        print("Member not found.")
        return

    print("\nMEMBER DETAILS")
    print(f"Member ID: {member['member_id']}")
    print(f"Name: {member['name']}")
    print(f"Course/Branch: {member['course']}")
    print(f"Semester: {member['semester']}")
    print(f"Email: {member['email'] or 'Not provided'}")
    print(f"Date joined: {member['date_joined']}")
    print(f"Active: {'Yes' if member['active'] else 'No'}")


def update_member(data):
    """Update member information."""
    member_id = get_non_empty_input("Enter member ID to update: ")
    member = find_member(data, member_id)

    if member is None:
        print("Member not found.")
        return

    member["name"] = get_optional_text("Name", member["name"])
    member["course"] = get_optional_text("Course/Branch", member["course"])
    member["semester"] = get_optional_text("Semester", member["semester"])
    member["email"] = get_optional_text("Email", member["email"])

    print("Member updated successfully.")


def delete_member(data):
    """Delete a member if they have no active transaction."""
    member_id = get_non_empty_input("Enter member ID to delete: ")
    member = find_member(data, member_id)

    if member is None:
        print("Member not found.")
        return

    has_active_transaction = any(
        transaction["member_id"] == member_id
        and transaction["status"] == "issued"
        for transaction in data["transactions"]
    )

    if has_active_transaction:
        print("Cannot delete a member with an active issued book.")
        return

    data["members"].remove(member)
    print("Member deleted successfully.")


def member_exists(data, member_id):
    """Return True if a member exists."""
    return find_member(data, member_id) is not None
