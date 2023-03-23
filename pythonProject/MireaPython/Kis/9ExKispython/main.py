def main(my_list):
    last_array = []
    filtered_array = []
    for i in my_list:
        if len(list(filter(None, i))) != 0:
            filtered_array.append(list(filter(None, i)))
    for i in filtered_array:
        new_array = []
        new_array.append(str(int(float(i[0]) * 100)) + "%")
        if (i[1].split(':')[0] == "нет"):
            new_array.append("Не выполнено")
        else:
            new_array.append("Выполнено")
        elem = i[1].split(':')[1]
        new_array.append(elem[:6] + "-" + elem[6:])
        if new_array not in last_array:
            last_array.append(new_array)
    return last_array


table = [
    ["0.7", "да:689-4027", "0.7"],
    ["0.1", "нет:410-5805", "0.1"],
    ["0.1", "нет:410-5805", "0.1"],
    [None, None, None],
    [None, None, None],
    ["0.1", "нет:410-5805", "0.1"],
    ["0.5", "нет:066-1955", "0.5"],
    ["0.4", "нет:682-3291", "0.4"]
]

print(main(table))
