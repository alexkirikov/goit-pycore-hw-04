import sys
from pathlib import Path
from colorama import init, Fore, Style

# Автоматичний ресет кольорів
init(autoreset=True)

def show_dir(path: Path, indent=0):
    for item in path.iterdir():
        prefix = " " * indent + "--"
        if item.is_dir():
            print(prefix + Fore.BLUE + item.name)
            show_dir(item, indent + 4)
        else:
            print(prefix + Fore.GREEN + item.name)

def main():
    if len(sys.argv) < 2:
        print("Вкажіть шлях до директорії!")
        return

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print("Шлях не існує!")
        return

    if not dir_path.is_dir():
        print("Вказаний шлях не є директорією!")
        return

    print(Fore.YELLOW + f"\nСтруктура директорії: {dir_path}\n")
    show_dir(dir_path)


if __name__ == "__main__":
    main()
