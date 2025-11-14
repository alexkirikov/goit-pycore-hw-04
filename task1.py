def total_salary(path: str):
    try:
        total = 0
        count = 0

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    _, salary = line.split(",")
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Помилка у рядку: {line}")

        if count == 0:
            return 0, 0

        average = total / count
        return total, average

    except FileNotFoundError:
        print("Файл не знайдено!")
        return 0, 0


if __name__ == "__main__":
    total, avg = total_salary("data/salary.txt")
    print(f"Загальна сума: {total}, Середня зарплата: {avg}")
