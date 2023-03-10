import re

def main(string):
    exp = r'@"(\w+)"\s*=\s*(-*\d+)'
    matches = re.findall(exp, string)
    dictionary = {}
    for match in matches:
        key = match[0]
        values = match[1]
        dictionary[key] = values
    return list(dictionary.items())

print(main('[ <data> set @"arerre_209" =-4948 </data><data>set @"zaen" = -5816 </data> ]'))
print(main('[<data>set @"este_583" = 5840 </data> <data> set @"usbear" = -2370 </data> <data>set @"arso_10" = -1480 </data><data>set @"vesobi"= 2526 </data> ]'))