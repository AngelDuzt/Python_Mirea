import struct


def read_b(data, address):
    result = {}
    for b_address in struct.unpack('>I', data[address: address + 4]):
        b1 = struct.unpack('>I', data[b_address: b_address + 4])[0]
        b2 = struct.unpack('>I', data[b_address + 4: b_address + 8])[0]
        return dict(B1=b1, B2=b2)


def read_d(data, address):
    result = []
    for i in range(0, 18, 6):
        d = struct.unpack('>1f1h', data[address + i: address + i + 6])
        result.append({
            'D1': d[0],
            'D2': d[1]
        })
    return result


def main(data):
    a1 = struct.unpack('>Q', data[5:13])[0]
    a2 = read_b(data, 13)
    a3 = struct.unpack('>IH', data[17: 23])
    a3 = struct.unpack('>' + 'b' * a3[0], data[a3[1]:a3[1] + a3[0]])
    a3 = "".join(list(map(chr, a3)))
    c1 = read_d(data, 23)
    c2 = struct.unpack('>2H', data[41:45])
    c2 = list(struct.unpack('>' + 'b' * c2[0], data[c2[1]:c2[1] + c2[0]]))
    a5 = struct.unpack('>h', data[45:47])[0]
    a6 = list(struct.unpack('>8h', data[47:63]))
    a7 = struct.unpack('>i', data[63:67])[0]
    a8 = struct.unpack('>2I', data[67: 75])
    a8 = list(struct.unpack('>' + 'H' * a8[0], data[a8[1]:a8[1] + a8[0] * 2]))
    return dict(A1=a1, A2=a2, A3=a3,
                A4=dict(C1=c1, C2=c2), A5=a5, A6=a6, A7=a7, A8=a8)


print(main((b'UNAL\x00X\x98jM/\xb2wp\x00\x00\x00K\x00\x00\x00\x03\x00S\xbf\n\xd9\xe3\x0e'
            b'\xbf?\x05\xddY\x9dM>\x08=%\x0c\x13\x00\x02\x00V\x82\xefN\xb2\xecv\xb8'
            b"\xe6\x7f\x8eTS\xf3\xfb`Q'\xf3\xfeM\xde#\x00\x00\x00\x05\x00\x00\x00X\xfeQRk$"
            b'.\xc9\x00xtw\xe1t\x0e{\xbe\xd9\xa5;\xf5\xbf"\xbb')))
