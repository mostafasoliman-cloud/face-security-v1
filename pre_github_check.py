from pathlib import Path
import ast
import sys


ROOT = Path(__file__).resolve().parent

IGNORE_DIRS = {
    "venv",
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
}

REQUIRED_FILES = [
    "FaceSecurity/main.py",
    "FaceSecurity/enroll.py",
    "FaceSecurity/camera/camera_manager.py",
    "FaceSecurity/detection/face_detector.py",
    "FaceSecurity/recognition/face_encoder.py",
    "FaceSecurity/recognition/face_matcher.py",
    "FaceSecurity/database/face_database.py",
    "FaceSecurity/config/settings.py",
    "requirements.txt",
]


def print_header(title):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def get_python_files():
    files = []

    for path in ROOT.rglob("*.py"):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue

        files.append(path)

    return files


def check_python_syntax():
    print_header("1. PYTHON SYNTAX CHECK")

    errors = []

    for file in get_python_files():
        try:
            source = file.read_text(
                encoding="utf-8"
            )

            ast.parse(source)

            print(f"[OK] {file.relative_to(ROOT)}")

        except Exception as error:
            errors.append(file)
            print(
                f"[ERROR] {file.relative_to(ROOT)}"
            )
            print(f"        {error}")

    return errors


def check_empty_files():
    print_header("2. EMPTY FILE CHECK")

    empty_files = []

    for file in get_python_files():

        if file.stat().st_size == 0:
            empty_files.append(file)

            print(
                f"[EMPTY] {file.relative_to(ROOT)}"
            )

    if not empty_files:
        print("[OK] No empty Python files found.")

    return empty_files


def check_required_files():
    print_header("3. REQUIRED FILES CHECK")

    missing = []

    for relative_path in REQUIRED_FILES:

        path = ROOT / relative_path

        if path.exists():
            print(f"[OK] {relative_path}")
        else:
            missing.append(path)
            print(f"[MISSING] {relative_path}")

    return missing


def check_requirements():
    print_header("4. REQUIREMENTS CHECK")

    requirements = ROOT / "requirements.txt"

    if not requirements.exists():
        print("[ERROR] requirements.txt not found.")
        return False

    content = requirements.read_text(
        encoding="utf-8"
    ).strip()

    if not content:
        print("[ERROR] requirements.txt is empty.")
        return False

    print("[OK] requirements.txt exists.")
    print()
    print(content)

    return True


def check_sensitive_files():
    print_header("5. SENSITIVE FILE CHECK")

    sensitive_names = {
        ".env",
        ".env.local",
        ".env.production",
        "credentials.json",
        "service-account.json",
        "id_rsa",
        "id_rsa.pub",
    }

    found = []

    for path in ROOT.rglob("*"):

        if not path.is_file():
            continue

        if any(part in IGNORE_DIRS for part in path.parts):
            continue

        if path.name.lower() in {
            name.lower()
            for name in sensitive_names
        }:
            found.append(path)

            print(
                f"[WARNING] {path.relative_to(ROOT)}"
            )

    if not found:
        print("[OK] No obvious sensitive files found.")

    return found


def check_pycache():
    print_header("6. PYTHON CACHE CHECK")

    caches = []

    for path in ROOT.rglob("__pycache__"):

        if any(part in {"venv", ".git"} for part in path.parts):
            continue

        caches.append(path)

        print(
            f"[WARNING] {path.relative_to(ROOT)}"
        )

    if not caches:
        print("[OK] No project __pycache__ folders found.")

    return caches


def check_gitignore():
    print_header("7. GITIGNORE CHECK")

    gitignore = ROOT / ".gitignore"

    if not gitignore.exists():
        print("[WARNING] .gitignore does not exist.")
        return False

    content = gitignore.read_text(
        encoding="utf-8"
    )

    required_patterns = [
        "venv",
        "__pycache__",
        "*.pyc",
        ".env",
    ]

    missing_patterns = []

    for pattern in required_patterns:

        if pattern not in content:
            missing_patterns.append(pattern)

    if missing_patterns:

        print("[WARNING] Missing .gitignore patterns:")

        for pattern in missing_patterns:
            print(f"  - {pattern}")

        return False

    print("[OK] .gitignore contains basic patterns.")

    return True


def check_duplicate_source_folders():
    print_header("8. DUPLICATE SOURCE FOLDER CHECK")

    source_names = {
        "camera",
        "config",
        "database",
        "detection",
        "recognition",
        "security",
        "utils",
    }

    duplicates = []

    for name in source_names:

        root_folder = ROOT / name
        project_folder = ROOT / "FaceSecurity" / name

        if root_folder.exists() and project_folder.exists():

            duplicates.append(name)

            print(
                f"[WARNING] Duplicate folder: {name}"
            )

    if not duplicates:
        print("[OK] No duplicate source folders found.")

    return duplicates


def main():

    print()
    print("FACE SECURITY - PRE GITHUB CHECK")
    print(f"Project: {ROOT}")

    syntax_errors = check_python_syntax()
    empty_files = check_empty_files()
    missing_files = check_required_files()
    requirements_ok = check_requirements()
    sensitive_files = check_sensitive_files()
    pycache = check_pycache()
    gitignore_ok = check_gitignore()
    duplicates = check_duplicate_source_folders()

    print_header("FINAL RESULT")

    problems = (
        len(syntax_errors)
        + len(empty_files)
        + len(missing_files)
        + len(sensitive_files)
        + len(pycache)
        + len(duplicates)
    )

    if not requirements_ok:
        problems += 1

    if not gitignore_ok:
        problems += 1

    if problems == 0:

        print("STATUS: READY FOR GITHUB")
        print()
        print("No major project-structure problems detected.")

        sys.exit(0)

    else:

        print("STATUS: REVIEW REQUIRED")
        print()
        print(f"Problems found: {problems}")
        print()
        print("Fix the warnings/errors above before pushing.")

        sys.exit(1)


if __name__ == "__main__":
    main()