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
