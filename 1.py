with open("F1.txt", "w") as f1:
    while True:
        line = input("Введите строку (пустая строка для завершения ввода): ")
        if not line:
            break
        f1.write(line)

with open("F1.txt", "r") as f1, open("F2.txt", "w") as f2:
    count_words = 0
    for line in f1:
        if line[0] == "A":
            f2.write(line)
            count_words += len(line.split())

print(f"Количество слов в F2: {count_words}")
