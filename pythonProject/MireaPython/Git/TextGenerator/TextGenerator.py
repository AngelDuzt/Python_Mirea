import random
def report_generate():
    first_List = ['Коллеги, ', 'В тоже время, ', 'Однако, ', 'Тем не менее, ', 'Следовательно, ',
              'Соответственно, ', 'Вместе с тем, ', 'С другой стороны, ']
    second_List = ['парадигма цифровой экономики ', 'контекст цифровой трансляции ', 'диджитализация бизнесс-процессов ',
               'прагматичный подход к цифровым платформам ', 'совокупность сквозных технологий ', 'программа прорывных исследований ',
               'ускорение блокчейн-транзакций ', 'экспоненциальный рост Big Data ']
    third_List = ['открывает новых возможности для ', 'выдвигает новые требования ', 'несет в себе риски ', 'расширяет горизонты ',
              'заставляет искать варианты ', 'не оставляет шанса для ', 'повышает вероятность ', 'обостряет проблему ']
    fourth_List = ['дальнейшего углубления ', 'бюджетного финансирования ', 'синергетического эффекта ', 'компрометации конфиденциальных ',
               'универсальной коммодитизации ', 'несанкционированной кастомизации ', 'нормативного регулирования ', 'практического применения ']
    fith_List = ['знаний и компетенций.', 'непроверенных гипотез.', 'волатильных активов.', 'опасных эксперементов.', 'государственно-частных партнерств.',
             'цифровых следов граждан.', 'нежелательных последствий.', 'внезапных открытий.']

    for i in range (3):
        for j in range (3):
            print(random.choice(first_List) + random.choice(second_List) + random.choice(third_List) +
                  random.choice(fourth_List) + random.choice(fith_List))
        print('\n')

report_generate()