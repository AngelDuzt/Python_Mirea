class MealyAutomat:
    def __init__(self):
        self.state = 'A'

    def type(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'C':
            self.state = 'F'
            return 6
        if self.state == 'F':
            self.state = 'G'
            return 9
        raise MealyError('type')

    def stare(self):
        if self.state == 'A':
            self.state = 'E'
            return 1
        if self.state == 'C':
            self.state = 'A'
            return 5
        if self.state == 'D':
            self.state = 'E'
            return 7
        if self.state == 'G':
            self.state = 'C'
            return 11
        if self.state == 'B':
            self.state = 'H'
            return 3
        raise MealyError('stare')

    def chip(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'C':
            self.state = 'D'
            return 4
        if self.state == 'E':
            self.state = 'F'
            return 8
        if self.state == 'G':
            self.state = 'H'
            return 10
        raise MealyError('chip')


class MealyError(Exception):
    pass


def main():
    return MealyAutomat()


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as ex:
        assert type(ex) == error
    assert output is None


def test():
    o = main()
    assert o.type() == 0  # 0
    assert o.chip() == 2  # 2
    assert o.chip() == 4  # 4
    assert o.stare() == 7  # 7
    assert o.chip() == 8  # 8
    assert o.type() == 9  # 9
    raises(lambda: o.type(), MealyError)
    assert o.stare() == 11  # 11
    assert o.stare() == 5  # 5
    assert o.stare() == 1  # 1
    assert o.chip() == 8  # 8
    raises(lambda: o.chip(), MealyError)
    raises(lambda: o.stare(), MealyError)
    assert o.type() == 9  # 9
    assert o.stare() == 11  # 11
    assert o.stare() == 5  # 6
    assert o.type() == 0  # 9
    assert o.stare() == 3  # 10
    o = main()
    assert o.type() == 0  # 0
    assert o.chip() == 2  # 2
    assert o.type() == 6
    assert o.type() == 9
    assert o.chip() == 10
