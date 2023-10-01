with open("Результаты соревнований.txt", "r") as file:
    results = []

    for line in file:
        parts = line.split()
        if len(parts) == 2:
            surname = parts[0]
            result = int(parts[1])
            results.append((surname, result))

# Сортируем результаты по убыванию, чтобы первое место было первым в списке
results.sort(key=lambda x: x[1], reverse=True)

if len(results) == 0:
    print("Файл пуст")
if len(results) >= 1:
    print(f"Первое место: {results[0][0]} с результатом {results[0][1]}")
if len(results) >= 2:
    print(f"Второе место: {results[1][0]} с результатом {results[1][1]}")
if len(results) >= 3:
    print(f"Третье место: {results[2][0]} с результатом {results[2][1]}")
