# Library Management System

A modular, CLI-based Python application designed to streamline library administration tasks, including inventory control, member registration, book transactions (issuing/returning), multi-field searching, and reporting. The system uses local JSON storage for persistent data management without external database dependencies.

## Overview of the Project

The **Library Management System** simplifies day-to-day library operations by replacing manual registers and unstructured logs. Built with clean, modular Python architecture, it allows librarians to manage books and members, track active loans, automatically compute due dates based on a 7-day loan policy, detect overdue returns, and inspect real-time library usage statistics.

## Features

* **Book Management**:
  * Add new books with detailed fields (title, author, category, publisher, publication year, total copies).
  * View all books or filter to show only available titles.
  * Update existing book records while maintaining copy constraints.
  * Guarded book deletion (prevents deleting books that currently have issued copies).

* **Member Management**:
  * Register new members (name, course/branch, semester, email).
  * View all registered members or retrieve individual member profiles.
  * Update member details.
  * Guarded member deletion (prevents deleting members with active book loans).

* **Issue & Return Operations**:
  * Issue books to active members with dynamic check on copy availability.
  * Automated 7-day due date calculation using Python's `datetime` module.
  * Return books using active transaction IDs, automatically updating available copy counts.
  * Automatic detection and reporting of late returns.
  * View all currently issued books with loan details.

* **Search Capabilities**:
  * Case-insensitive search across book attributes (ID, title, author, category).
  * Case-insensitive search across member attributes (ID, name, course, semester).

* **Library Reports**:
  * High-level statistics summary (total titles, total copies, available copies, issued copies, total members, active members, total transactions).
  * Dedicated overdue books report identifying unreturned items past their due date.
  * Category report breaking down book title counts by genre/category.

* **Data Persistence & Safety**:
  * Structured storage using `data/library_data.json`.
  * Automatic file creation on first launch.
  * Graceful error handling for missing or corrupted JSON files with automatic recovery defaults.
  * Auto-generated sequential formatted IDs (`B001`, `M001`, `T001`).

## Technologies/Tools Used

* **Programming Language**: Python 3.x
* **Standard Libraries**:
  * `json`: Parsing, serializing, and managing local JSON data persistence.
  * `pathlib`: Managing cross-platform relative file paths (`Path`).
  * `datetime`: Operations involving dates, 7-day loan periods (`timedelta`), and overdue date comparisons.

## Steps to Install & Run the Project

### Prerequisites

Ensure Python 3.x is installed on your operating system. You can verify your installation by running:

```bash
python --version
```

*or*

```bash
python3 --version
```

### Directory Structure

Ensure your project directory contains the following file structure:

```text
.
├── books.py
├── issue_return.py
├── main.py
├── members.py
├── README.md
├── reports.py
├── search.py
├── statement.md
├── utils.py
└── data/ (Auto-created on first run)
    └── library_data.json
```

### Execution Steps

1. Open your terminal or command prompt.
2. Navigate to the root directory containing the project files:
   ```bash
   cd path/to/your/project-folder
   ```
3. Launch the application:
   ```bash
   python main.py
   ```
   *(Note: Use `python3 main.py` on Linux/macOS systems if required).*

## Instructions for Testing

Follow this step-by-step testing sequence to verify all submodules:

1. **System Initialization Test**:
   * Run `python main.py`.
   * Verify that the `data/library_data.json` file is automatically created inside the `data` directory upon starting.

2. **Book & Member Creation**:
   * Select option `1` (**Book Management**) -> `1` (**Add Book**). Enter details for a new book. Confirm that a unique ID such as `B001` is assigned.
   * Return to main menu, select option `2` (**Member Management**) -> `1` (**Add Member**). Enter details for a new member. Confirm that a unique ID such as `M001` is assigned.

3. **Issue & Safety Constraints Test**:
   * Go to option `3` (**Issue / Return Book**) -> `1` (**Issue Book**). Enter book ID `B001` and member ID `M001`. Confirm transaction ID `T001` is created and a due date set exactly 7 days from today is displayed.
   * Go to `1` (**Book Management**) -> `5` (**Delete Book**) and attempt to delete `B001`. Confirm the system blocks deletion due to active issued copies.
   * Go to `2` (**Member Management**) -> `5` (**Delete Member**) and attempt to delete `M001`. Confirm the system blocks deletion due to active issued books.

4. **Return & Reports Test**:
   * Go to option `3` (**Issue / Return Book**) -> `2` (**Return Book**) and supply `T001`. Confirm successful return and copy count incrementation.
   * Go to option `4` (**Search**) and test keyword searching across title, author, or member names.
   * Go to option `5` (**Library Reports**) -> `1` (**Library Summary**) to view dynamically calculated overall statistics.

## Screenshots

*(Terminal screenshots demonstrating application workflow)*

### Main Menu Interface

```text
============================================================
LIBRARY MANAGEMENT SYSTEM
============================================================
1. Book Management
2. Member Management
3. Issue / Return Book
4. Search
5. Library Reports
6. Exit
Enter your choice: 
```

### Adding a Book Record

```text
BOOK MANAGEMENT
------------------------------------------------------------
1. Add Book
2. View All Books
3. View Available Books
4. Update Book
5. Delete Book
6. Back
Enter your choice: 1
Enter book title: Operating System Concepts
Enter author name: Abraham Silberschatz
Enter category: Computer Science
Enter publisher: Wiley
Enter publication year: 2018
Enter total copies: 5
Book added successfully. Book ID: B001
```

### Issuing a Book

```text
ISSUE / RETURN BOOK
------------------------------------------------------------
1. Issue Book
2. Return Book
3. View Issued Books
4. Back
Enter your choice: 1
Enter book ID: B001
Enter member ID: M001
Book issued successfully.
Transaction ID: T001
Due date: 2026-10-03
```
