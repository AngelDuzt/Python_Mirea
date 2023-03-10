import sys


def myPrint(*args):
    for arg in args:
        if type(arg) == str:
            sys.stdout.write(arg + '\n')
        elif type(arg) == list:
            LeftBracket, RightBracket = '[', ']'
            sys.stdout.write(LeftBracket)
            for i in arg:
                sys.stdout.write(str(i))
                if(i != arg[-1]):
                    sys.stdout.write(', ')
            sys.stdout.write(RightBracket + '\n')
        elif type(arg) == tuple:
            LeftBracket, RightBracket = '(', ')'
            sys.stdout.write(LeftBracket)
            for i in arg:
                sys.stdout.write(str(i))
                if(i != arg[-1]):
                    sys.stdout.write(', ')
            sys.stdout.write(RightBracket + '\n')
        elif type(arg) == bool:
            sys.stdout.write(str(arg) + '\n')
        elif type(arg) == int:
            sys.stdout.write(str(arg) + '\n')
        else:
            LeftBracket, RightBracket = '{', '}'
            sys.stdout.write(LeftBracket)
            counter = 0
            for i in arg.items():
                sys.stdout.write(chr(39) + str(i[0]) + chr(39) + ': ' + str(i[1]))
                if counter != len((arg.items())) - 1:
                    sys.stdout.write(', ')
                counter += 1
            sys.stdout.write(RightBracket + '\n')
dict1 = {'qwe': 1, 'qe': 2, 'q': 3}
list1 = [1, 2, 3]
tuple1 = ("Fred", 13, [5, 7, 4])
string1 = "Hello World!"
boolean = True
integer = 13231
myPrint(dict1)
myPrint(list1)
myPrint(tuple1)
myPrint(string1)
myPrint(boolean)
myPrint(integer)
myPrint(dict1, list1)