def find_common_participants(participants_first_group, participants_second_group, razdelitel = ','):
    group1, group2 = set(participants_first_group.split(razdelitel)), set(participants_second_group.split(razdelitel))
    return sorted(list(group1 & group2))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
