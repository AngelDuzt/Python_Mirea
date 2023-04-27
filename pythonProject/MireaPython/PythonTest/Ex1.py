def is_harshad_number(number):
    if number % sum(map(int, str(number))) == 0:
        print("Yes, it is harshad number")
    else: print("No, it isnot")

is_harshad_number(195)
