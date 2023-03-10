def main(string):
    int_value = int(string[2:], 16)
    N1 = int_value & 0b000_00_0000000_000000_111111
    N2 = int_value >> 6 & 0b000_00_0000000_111111
    N3 = int_value >> 12 & 0b000_00_1111111
    N4 = int_value >> 19 & 0b000_11
    N5 = int_value >> 21 & 0b111
    return dict(zip(['N1', 'N2', 'N3', 'N4', 'N5'], [N1, N2, N3, N4, N5]))

print(main('0xb9a562'))
