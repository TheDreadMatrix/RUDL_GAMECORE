import keyword
import re

import ast
import os





def check_security(parser):
    project_name = os.getenv("RUDLGC_PROJECT_NAME")

    if not project_name:
        parser.error("Project name not found in RUDLGC_PROJECT_NAME")

    base_path = os.path.abspath(project_name)

    if not os.path.exists(base_path):
        parser.error(f"Project folder not found: {base_path}")

    violations = []

    for root, _, files in os.walk(base_path):
        for file in files:
            if not file.endswith(".py"):
                continue

            file_path = os.path.join(root, file)

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    tree = ast.parse(f.read(), filename=file_path)
            except Exception:
                continue

            for node in ast.walk(tree):

                # 🔴 IMPORT
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        name = alias.name.split(".")[0]

                        if name == "rudlgc":
                            continue

                        if name in _PROHIBITED_WORDS:
                            violations.append((file_path, f"import {name}"))

                # 🔴 FROM IMPORT
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        name = node.module.split(".")[0]

                        if name == "rudlgc":
                            continue

                        if name in _PROHIBITED_WORDS:
                            violations.append((file_path, f"from {name} import ..."))

                # 🔴 FUNCTION CALL
                elif isinstance(node, ast.Call):

                    # случай: eval(...)
                    if isinstance(node.func, ast.Name):
                        func_name = node.func.id

                        if func_name in _PROHIBITED_FUNCTIONS:
                            violations.append((file_path, f"call to {func_name}()"))

                    # случай: os.system(...)
                    elif isinstance(node.func, ast.Attribute):
                        value = node.func.value

                        if isinstance(value, ast.Name):
                            obj_name = value.id
                            attr_name = node.func.attr

                            # запрещаем os.*
                            if obj_name in _PROHIBITED_WORDS:
                                violations.append(
                                    (file_path, f"{obj_name}.{attr_name}()")
                                )

    if violations:
        messages = []
        for path, issue in violations:
            messages.append(f"{path} -> {issue}")

        parser.error(
            "Security violation: prohibited imports or function usage detected.\n"
            "Do not use restricted modules or dangerous functions.\n\n"
            + "\n".join(messages)
        )





_PROHIBITED_WORDS = [
    "os",
    "sys",
    "importlib",
    "traceback",
    "signal",
    "pickle",
    "marshal",
    "rudlgc",
    "nigga",
    "rudlgc",
    "test",
    "pygame",
    "pygaeme-ce",
    "moderngl",
    "rudleg",
    "rudlpp",
    "audio",
    "camera",
    "core",
    "contrib",
    "render",
    "stuff",
    "sdl2",
]

_PROHIBITED_FUNCTIONS = [
    "getattr",
    "setattr",
    "delattr",
    "eval",
    "exec",
    "__import__",
    "compile",
    "open",        
    "input",
]

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