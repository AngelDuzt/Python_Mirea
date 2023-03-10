def main(x):
    bin_x = int(x)
    S1 = bin_x & ((1 << 3) - 1)
    S2 = (bin_x >> 3) & ((1 << 4) - 1)
    S4 = (bin_x >> 17) & ((1 << 10) - 1)
    S5 = (bin_x >> 27) & ((1 << 11) - 1)
    #print(C1, C2, C3, C4, C3 + C1 + C2 + C4, bin_x)
    return str(hex(S4 | S1 << 20 | S5 << 23 | S2 << 33))

print(main('239948252'))

