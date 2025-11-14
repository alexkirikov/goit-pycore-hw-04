from pprint import pprint

def get_cats_info(path: str):
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    cat_id, name, age = line.split(",")
                    cats.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    print(f"Помилка формату рядка: {line}")
        return cats

    except FileNotFoundError:
        print("Файл не знайдено!")
        return []


if __name__ == "__main__":
    cats = get_cats_info("data/cats.txt")
    pprint(cats, sort_dicts=False)
