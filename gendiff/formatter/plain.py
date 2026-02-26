def format_plain(diff):
    lines = []
    walk(diff, lines)
    return "\n".join(lines)


def walk(diff, lines, parent=""):
    for node in diff:
        key = node["key"]
        status = node["type"]

        property_name = f"{parent}.{key}" if parent else key

        if status == "nested":
            walk(node["children"], lines, property_name)

        elif status == "added":
            value = format_value(node["value"])
            lines.append(
                f"Property '{property_name}' was added with value: {value}"
            )

        elif status == "removed":
            lines.append(
                f"Property '{property_name}' was removed"
            )

        elif status == "changed":
            old = format_value(node["old_value"])
            new = format_value(node["new_value"])
            lines.append(
                f"Property '{property_name}' was updated. From {old} to {new}"
            )

        # unchanged пропускаем


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"

    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"

    if isinstance(value, str):
        return f"'{value}'"

    return str(value)