import pytest
import random
import string

import ch01


@pytest.fixture
def sample_estimates():
    return ch01.PlanningPoker({'Ted': 2, 'Barney': 4, 'Lily': 8, 'Robin': 16})

def test_reject_null_input():
    with pytest.raises(TypeError):
        c = ch01.PlanningPoker()

def test_reject_empty_list():
    c = ch01.PlanningPoker({})
    with pytest.raises(AssertionError):
        c.return_extremes()

def test_reject_single_estimate():
    c = ch01.PlanningPoker({'abc': 1})
    with pytest.raises(AssertionError):
        c.return_extremes()

def test_with_two_elements():
    c = ch01.PlanningPoker({'Mauricio': 10, 'Frank': 5})
    assert sorted(c.return_extremes()) == sorted(["Mauricio", "Frank"])

def test_with_three_elements():
    c = ch01.PlanningPoker({'Mauricio': 10, 'Arie': 5, "Frank": 7})
    assert sorted(c.return_extremes()) == sorted(["Mauricio", "Arie"])

def test_in_any_order():
    elms = [('Mauricio', 10), ('Frank', 5), ('Arie', 7)]
    random.shuffle(elms)
    c = ch01.PlanningPoker(dict(elms))
    assert sorted(c.return_extremes()) == sorted(["Mauricio", "Frank"])

def test_with_random():
    elms = [('Highest', 10), ('Lowest', 1)]
    letters = string.ascii_lowercase
    for i in range(8):
        str = ''.join(random.choice(letters) for i in range(5))
        elms.append((str, random.randint(2, 9)))
    random.shuffle(elms)
    c = ch01.PlanningPoker(dict(elms))
    assert sorted(c.return_extremes()) == sorted(["Highest", "Lowest"])

def test_with_duplicates():
    c = ch01.PlanningPoker({'Mauricio': 10, 'Arie': 5,
                            'Andy': 10, 'Annibale': 5, "Frank": 7})
    assert sorted(c.return_extremes()) == sorted(["Mauricio", "Arie"])
