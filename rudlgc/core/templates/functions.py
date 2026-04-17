import keyword
import re

def is_valid_name(name: str) -> bool:
    if not name:
        return False

    if not (name[0].isalpha() or name[0] == "_"):
        return False
    
    if re.search(r"[^a-zA-Z0-9_]", name):
        return False

    if keyword.iskeyword(name):
        return False

    return True


def _group_by_category(settings, category_map):
    grouped = {}

    # reverse map: variable -> category
    reverse_map = {}

    for category, vars_list in category_map.items():
        for var in vars_list:
            reverse_map[var] = category

    for name, value in settings:
        group = reverse_map.get(name, "OTHER")

        if group not in grouped:
            grouped[group] = []

        grouped[group].append((name, value))

    return grouped