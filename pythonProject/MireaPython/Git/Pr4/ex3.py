def main(string):
    int_value = int(string[2:], 16)
    mylist = []
    R1 = int_value & 0b000000_000_000_000000000_1111
    mylist.append(('R1', R1))
    R2 = int_value >> 4 & 0b000000_000_000_000011111_1111
    mylist.append(('R2', R2))
    R3 = int_value >> 13 & 0b000000_000_111_000000000_0111
    mylist.append(('R3', R3))
    R4 = int_value >> 16 & 0b000000_111_000_000000000_0111
    mylist.append(('R4', R4))
    R5 = int_value >> 19 & 0b111111_000_000_000000011_1111
    mylist.append(('R5', R5))
    return mylist

print(main('0x6a9f6'))
