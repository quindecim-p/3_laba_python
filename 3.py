with open("subjects.txt", "r", encoding="utf-8") as file:
    subject_info = {}

    for line in file:
        parts = line.split(":")
        if len(parts) == 2:
            subject_name = parts[0]
            info_part = parts[1]
            lessons_info = info_part.split()

            total_lessons = 0

            # Обходим подстроки и суммируем количество занятий
            for lesson in lessons_info:
                num_str = ""
                for char in lesson:
                    if char.isdigit():
                        num_str += char
                    else:
                        break
                if num_str:
                    total_lessons += int(num_str)

            subject_info[subject_name] = total_lessons

print(subject_info)
