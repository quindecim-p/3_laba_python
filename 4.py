import json


with open("companies.txt", "r", encoding="utf-8") as file:
    company_profits = []

    total_profit = 0
    firm_count = 0

    for line in file:
        parts = line.split()
        if len(parts) == 4:
            firm_name = parts[0]
            revenue = int(parts[2])
            expenses = int(parts[3])

            profit = revenue - expenses

            company_profits.append({firm_name: profit})

            if profit > 0:
                total_profit += profit
                firm_count += 1

    average_profit = total_profit / firm_count

# Создаем список, содержащий словарь с прибылью фирм и словарь со средней прибылью
result_list = [company_profits, {"average_profit": average_profit}]

with open("company_profits.json", "w") as json_file:
    json.dump(result_list, json_file)

print(result_list)
