def main(args):
    dict1 = {1966: 0, 2017: 1, 2010: 2}
    dict2 = {1966: 3, 2017: 4, 2010: 5}
    dict3 = {1966: 7, 2017: 8, 2010: 9}
    dict4 = {2010: 10, 1987: 11}
    dict5 = {1996: 13, 1981: 14}
    if args[4] != 2002:
        return dict5.get(args[4])
    else:
        if args[0] == 2003:
            return 12
        elif args[0] == 1972:
            if args[3] != 2006:
                return dict4.get(args[3])
            else:
                return dict3.get(args[1])
        else:
            if args[3] == 1987:
                return 6
            elif args[3] == 2010:
                return dict2.get(args[1])
            else:
                return dict1.get(args[1])
