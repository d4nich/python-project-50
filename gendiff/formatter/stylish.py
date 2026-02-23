def format_primitive(value):
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    return str(value)


def stringify(value, depth):
    if not isinstance(value, dict):
        return format_primitive(value)

    indent_size = 4
    current_indent = " " * (depth * indent_size)
    closing_indent = " " * ((depth - 1) * indent_size)

    lines = []
    for k, v in value.items():
        lines.append(f"{current_indent}{k}: {stringify(v, depth + 1)}")

    return "{\n" + "\n".join(lines) + "\n" + closing_indent + "}"


def get_indents(depth, indent_size=4):
    current = " " * (depth * indent_size)
    marker = " " * (depth * indent_size - 2)
    closing = " " * ((depth - 1) * indent_size)
    return current, marker, closing


def format_stylish(diff, depth=1):
    lines = []
    current_indent, marker_indent, _ = get_indents(depth)

    for node in diff:
        key = node["key"]
        status = node["type"]

        if status == "nested":
            value = format_stylish(node["children"], depth + 1)
            lines.append(f"{current_indent}{key}: {value}")

        elif status == "added":
            lines.append(
            f"{marker_indent}+ {key}: {stringify(node['value'], depth + 1)}"
            )

        elif status == "removed":
            lines.append(
            f"{marker_indent}- {key}: {stringify(node['value'], depth + 1)}"
            )

        elif status == "unchanged":
            lines.append(
            f"{marker_indent}  {key}: {stringify(node['value'], depth + 1)}"
            )

        elif status == "changed":
            lines.append(
            f"{marker_indent}- {key}: {stringify(node['old_value'], depth + 1)}"
            )
            lines.append(
            f"{marker_indent}+ {key}: {stringify(node['new_value'], depth + 1)}"
            )

    _, _, closing_indent = get_indents(depth)
    result = "\n".join(lines)

    return "{\n" + result + "\n" + closing_indent + "}"
