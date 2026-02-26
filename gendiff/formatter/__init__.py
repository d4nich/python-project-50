from .plain import format_plain
from .stylish import format_stylish


def format_diff(diff, format_name):
    if format_name == "stylish":
        return format_stylish(diff)

    if format_name == "plain":
        return format_plain(diff)

    raise ValueError("Unknown format")
