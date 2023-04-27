def get_inheritance(OSError):
    return " -> ".join([c.__name__ for c in OSError.mro()])




print(get_inheritance(OSError))