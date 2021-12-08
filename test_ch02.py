

import ch02

def test_simple():
    assert ch02.substrings_between('abc', 'a', 'c') == ['b']
    assert ch02.substrings_between('axcaycazc', 'a', 'c') == ['x', 'y', 'z']