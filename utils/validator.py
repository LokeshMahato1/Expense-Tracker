def validate_amount(amount):
    # Check whether the amount is a valid positive number.
    try:
        return float(amount) > 0
    except ValueError:
        return False


def validate_expense(category, method):
    # Check required expense fields.
    return bool(category and method)