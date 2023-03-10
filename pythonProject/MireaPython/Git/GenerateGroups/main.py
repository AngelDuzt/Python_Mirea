Groups_list = ['ИВБО-01-21', 'ИВБО-02-21', 'ИВБО-03-21', 'ИВБО-04-21', 'ИКБО-01-21', 'ИКБО-02-21',
               'ИКБО-03-21', 'ИКБО-04-21', 'ИКБО-05-21', 'ИКБО-06-21', 'ИКБО-07-21', 'ИКБО-08-21', 'ИКБО-09-21',
               'ИКБО-10-21', 'ИКБО-11-21', 'ИКБО-12-21', 'ИКБО-13-21', 'ИКБО-14-21', 'ИКБО-15-21', 'ИКБО-16-21',
               'ИМБО-01-21', 'ИМБО-02-21', 'ИНБО-01-21', 'ИНБО-02-21',
               'ИНБО-03-21']

def generate_groups(group_list):
    groups = []
    for i in group_list:
        if i[0:4] not in groups:
            groups.append(i[0:4])
    for j in groups:
        print(j)
        counter = 0
        for i in group_list:
            if j in i:
                print(i, end=' ')
                counter += 1
                if counter == 10:
                    print()
        print('\n')
generate_groups(Groups_list)

