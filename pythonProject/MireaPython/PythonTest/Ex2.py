def is_eq_list(list_):
    return len(set(list_)) == len(list_)


print(is_eq_list([1, 2, 3])); print(is_eq_list([1]))