def res_str(array_str):
    for i in range(len(array_str) // 2):
        array_str[i], array_str[-1 - i] = array_str[-1 - i], array_str[i]
    str = ""
    for i in array_str:
        str += i
        if i != array_str[-1]:
            str += " "
    return str


def count_char(str, char):
    return str.count(char)


def count_characters(str):
    cnt = {}
    for i in str:
        cnt[i] = count_char(str, i)
    return cnt


str = res_str(["language!", "programming", "Python", "the", "love", "I"])
print(count_characters(str.lower()))
