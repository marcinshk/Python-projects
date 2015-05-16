
from nose.tools import *
from ex47.map import *

def test_polandArea():
    poland = Country('Poland', 'Warsaw', 350000)
    assert_equal(poland.getArea(), 350000)

    poland.setArea(poland.getArea() + 50000)
    assert_equal(poland.getArea(), 400000)

    poland.setArea(poland.getArea() + 50000)
    assert_equal(poland.getArea(), 400000)

def test_polandCapital():
    poland = Country('Poland', 'Warsaw', 350000)
    assert poland.getCapital() == 'Warsaw'

