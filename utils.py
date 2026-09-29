from datetime import datetime


DATE_FORMAT = "%Y-%m-%d"


def get_non_empty_input(prompt):
    """Get text that is not empty."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def get_positive_integer(prompt, allow_zero=False):
    """Get a valid positive whole number."""
    while True:
        value = input(prompt).strip()

        try:
            number = int(value)

            if allow_zero and number >= 0:
                return number

            if not allow_zero and number > 0:
                return number

            print("Please enter a valid positive number.")
        except ValueError:
            print("Invalid number. Please try again.")


def get_valid_date(prompt, allow_blank=False):
    """Get a date in YYYY-MM-DD format."""
    while True:
        value = input(prompt).strip()

        if allow_blank and value == "":
            return ""

        try:
            datetime.strptime(value, DATE_FORMAT)
            return value
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD.")


def get_optional_text(prompt, current_value):
    """Get new text or keep the old value."""
    value = input(f"{prompt} [{current_value}]: ").strip()
    return value if value else current_value


def find_record(records, key, value):
    """Find one record by a key and value."""
    for record in records:
        if str(record.get(key, "")).lower() == str(value).lower():
            return record
    return None


def generate_id(records, prefix, key):
    """Generate an unused ID using the highest existing number."""
    highest_number = 0

    for record in records:
        record_id = str(record.get(key, ""))
        if record_id.startswith(prefix):
            number_part = record_id[len(prefix):]
            if number_part.isdigit():
                highest_number = max(highest_number, int(number_part))

    return f"{prefix}{highest_number + 1:03d}"


def print_line():
    print("-" * 60)
