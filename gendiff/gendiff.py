from .build_diff import build_diff
from .formatter import format_diff
from .parser import parse_file


def generate_diff(file1, file2, format_name="stylish"):
    data1 = parse_file(file1)
    data2 = parse_file(file2)

    diff = build_diff(data1, data2)
    return format_diff(diff, format_name)