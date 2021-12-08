import pytest

import ch02

def test_simple():
    assert ch02.substrings_between('abc', 'a', 'c') == ['b']
    assert ch02.substrings_between('aabcdd', 'aa', 'dd') == ['bc']
    assert ch02.substrings_between('aabcddaa', 'aa', 'dd') == ['bc']
    assert ch02.substrings_between('axcaycazc', 'a', 'c') == ['x', 'y', 'z']

"""
1. test for empty input string
2. test for no input string
3. test for empty start/stop string
4. test for no start/stop string
5. test for start = input
6. test for start = stop
7. test for start = input = stop
8. test for input doesn't have start
9. test for input doesn't have stop
10. test for input = start + stop
input length = 1
input length > 1
start/stop = 1
start/stop > 1
"""

def test_input_null():
    assert ch02.substrings_between(None, "a", "b") is None

def test_input_empty():
    assert ch02.substrings_between("", "a", "b") == []

def test_open_null():
    with pytest.raises(TypeError):
        ch02.substrings_between("abc", None, "b")

def test_open_empty():
    assert ch02.substrings_between("abc", "", "b") is None

def test_close_null():
    with pytest.raises(TypeError):
        ch02.substrings_between("abc", "a", None)

def test_close_empty():
    assert ch02.substrings_between("abc", "a", "") is None

def test_input_len1():
    assert ch02.substrings_between("a", "a", "b") is None
    assert ch02.substrings_between("a", "b", "a") is None
    assert ch02.substrings_between("a", "b", "b") is None
    assert ch02.substrings_between("a", "a", "a") is None

def test_open_close_len1():
    assert ch02.substrings_between("abc", "x", "y") is None
    assert ch02.substrings_between("abc", "a", "y") is None
    assert ch02.substrings_between("abc", "x", "c") is None
    assert ch02.substrings_between("abc", "a", "c") == ["b"]
    assert ch02.substrings_between("abcabc", "a", "c") == ["b", "b"]

def test_open_close_diff_len():
    assert ch02.substrings_between("aabcc", "xx", "yy") is None
    assert ch02.substrings_between("aabcc", "aa", "yy") is None
    assert ch02.substrings_between("aabcc", "xx", "cc") is None
    assert ch02.substrings_between("aabbcc", "aa", "cc") == ["bb"]
    assert ch02.substrings_between("aabccaaeeccabcc", "aa", "cc") == ["b", "ee"]

def test_empty_between_open_close():
    assert ch02.substrings_between("aacc", "aa", "cc") == [""]


def test_add_lists_basic():
    assert ch02.add_lists_of_integers([1,2,3],[3,2,1]) == [4,4,4]
    assert ch02.add_lists_of_integers([1,2,3,4],[3,2,1]) == [1,5,5,5]
    assert ch02.add_lists_of_integers([1,2,3],[7,8,9]) == [9,1,2]
    assert ch02.add_lists_of_integers([1],[1]) == [2]
    assert ch02.add_lists_of_integers([1,5],[1,0]) == [2,5]
    assert ch02.add_lists_of_integers([1,5],[1,5]) == [3,0]
    assert ch02.add_lists_of_integers([5,0,0],[2,5,0]) == [7,5,0]

"""
1. empty
2. null
3. single digit
4. multiple digits
5. zeroes on the left
6. left length > right length
7. left length < right length
8. same length
*** bad input
1. alpha
2. negative number
3. > 9
4. float
*** test carry
1. sum without carry
2. one carry at the beginning
3. one carry in the middle
4. many carries
5. many carries - not in a row
6. carry propagated to new most signifacant number
"""

def test_add_null_empties():
    assert ch02.add_lists_of_integers(None, [7,2]) is None
    assert ch02.add_lists_of_integers([], [7,2]) == [7,2]
    assert ch02.add_lists_of_integers([9,8], None) is None
    assert ch02.add_lists_of_integers([9,8], []) == [9,8]
    assert ch02.add_lists_of_integers(None, None) is None

def test_add_bad_input():
    with pytest.raises(TypeError):
        ch02.add_lists_of_integers(["a",8], [1,2])
    with pytest.raises(TypeError):
        ch02.add_lists_of_integers([7,8], ["a",2])
    with pytest.raises(TypeError):
        ch02.add_lists_of_integers([-1,8], [1,2])
    with pytest.raises(TypeError):
        ch02.add_lists_of_integers([1,8], [1.1,2])



assert ch02.add_lists_of_integers([1], [1]) == [2]
