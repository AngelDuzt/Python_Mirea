import re


def main(string):
    exp = r"loc\s*#([-\w]+)\s->\s*q\((\w+)"
    matches = re.findall(exp, string)
    dictionary = {}
    for match in matches:
        key = match[1]
        values = int(match[0])
        dictionary[key] = values
    return list(dictionary.items())


print(main('{{ (loc#5163 -> q(lace). ) (loc #-9919 ->q(beonqu_319). ) ( loc #-7470 -> q(enve). ) }}'))
print(main('{{ ( loc#1375 -> q(teanbe).) ( loc #4362 -> q(diared_916). ) ( loc#-3581 ->q(raorbi_140). )}}'))
