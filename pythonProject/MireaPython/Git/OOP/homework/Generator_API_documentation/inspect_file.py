import inspect
import matplotlib

for name, data in inspect.getmembers(matplotlib):
    if name == '__doc__':
        print('Markdown\n# Модуль m\n', data)

trigger = 0

for name, data in inspect.getmembers(matplotlib, inspect.isclass):
    print(f'## Класс {name}\n\nОписание {name}.\n')
    for name_m, data_m in inspect.getmembers(data, inspect.isfunction):
        if name_m.startswith('__'):
            continue
        counter = 0
        for i in inspect.getsource(data_m):
            if i == '\n':
                break
            counter += 1
        print(f'* **Метод** ' + '`' + inspect.getsource(data_m)[8:counter-1] + '`' + f'\n\nОписание {name_m}.\n')

for name, data in inspect.getmembers(matplotlib, inspect.isfunction):
    if name.startswith('__'):
        continue
    counter = 0
    for i in inspect.getsource(data):
        if i == '\n':
            break
        counter += 1
    print(f'## Функция {name}\n\nСигнатура: `' + inspect.getsource(data)[4:counter-1] + f'`\n\nОписание {name}.')
