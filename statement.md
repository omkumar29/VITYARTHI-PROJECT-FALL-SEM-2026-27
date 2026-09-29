# Project Statement

## Problem Statement

Traditional paper-based or unorganized spreadsheet tracking in academic and public libraries often leads to inaccurate inventory levels, unmonitored book loans, untracked overdue returns, and inefficient manual search processes. Small-to-medium institutions require an efficient, lightweight, and automated software solution to streamline cataloging, member onboarding, loan administration, and operational reporting—without requiring complex server infrastructure or external database management systems.

## Scope of the Project

The project scope encompasses the design and implementation of a modular, Command Line Interface (CLI) Python application that automates primary library administrative tasks while maintaining localized persistent data storage.

### Included in Scope:

* **Inventory & Member Management**: Full CRUD (Create, Read, Update, Delete) workflows for cataloged books and registered members with input validation.
* **Transaction Administration**: Check-out and check-in workflows linked to real-time copy availability counts.
* **Policy & Constraint Enforcement**: Automatic 7-day loan due date generation, detection of late returns, and deletion guards blocking removal of records tied to active loans.
* **Persistent Data Management**: Automated JSON reading, parsing, writing, and corruption recovery fallback (`library_data.json`).
* **Data Querying & Reporting**: Keyword-based multi-field search engine alongside real-time statistics generation (summary, overdue listings, category breakdown).

### Excluded from Scope:

* Web-based frontends or graphical user interfaces (GUI).
* Multi-node relational databases (SQL/NoSQL database servers).
* User authentication and role-based privilege controls (e.g., admin vs. student logins).
* Monetary fine calculations or online payment integration.

## Target Users

* **Library Administrators & Staff**: Desk administrators who handle inventory registration, member profile creation, book issuing, and processing returns.
* **Academic/Department Librarians**: Institutional managers requiring real-time summaries, catalog auditing reports, and list tracking for overdue loans.

## High-Level Features

1. **Structured Command Line Navigation**
   * Hierarchical text menus providing intuitive navigation across management submodules.

2. **Automated Sequential ID Generator**
   * Auto-formatting identifier creation for books (`B001`), members (`M001`), and transactions (`T001`).

3. **Dynamic Copy Availability Tracking**
   * Real-time adjustment of `available_copies` versus `total_copies` upon issuing or returning books.

4. **Loan & Overdue System**
   * Automatic calculation of 7-day loan periods (`timedelta`) with late-return detection and dedicated overdue monitoring.

5. **Multi-Field Partial Text Search**
   * Case-insensitive keyword matching across multiple attributes for books (ID, title, author, category) and members (ID, name, course, semester).

6. **Analytical Library Reporting**
   * On-demand summary metrics, overdue book tracking logs, and category distribution breakdowns.
