def smalldet(args):
    return args[0][0] * args[1][1] - args[0][1] * args[1][0]

def main():
    print(smalldet([[3, 5], [5, 2]]))

if __name__ == '__main__':
    main()