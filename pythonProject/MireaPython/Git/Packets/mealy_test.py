from mealy_main import MealyError, main, raises
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
