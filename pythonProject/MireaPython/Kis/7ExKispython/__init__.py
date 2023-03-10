def main(x):
    bin_x = int(x)
    C1 = bin_x & ((1 << 6) - 1)
    C2 = (bin_x >> 6) & ((1 << 2) - 1)
    C3 = (bin_x >> 8) & ((1 << 9) - 1)
    C4 = (bin_x >> 17) & ((1 << 6) - 1)
    return str(hex(C4 | C2 << 6 | C1 << 8 | C3 << 14))
