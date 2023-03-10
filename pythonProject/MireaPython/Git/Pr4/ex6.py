def main(x):
    bin_x = int(x)
    C1 = bin_x & ((1 << 7) - 1)
    C2 = (bin_x >> 7) & ((1 << 3) - 1)
    C3 = (bin_x >> 10) & ((1 << 6) - 1)
    C4 = (bin_x >> 16) & ((1 << 4) - 1)
    #print(C1, C2, C3, C4, C3 + C1 + C2 + C4, bin_x)
    return str(C1 | C3 << 7 | C4 << 13 | C2 << 17)

print(main('743096'))

