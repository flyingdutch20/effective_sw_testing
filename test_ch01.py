import pytest
import random

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
    elms = [('Mauricio', 10), ('Frank', 5)]
    random.shuffle(elms)
    c = ch01.PlanningPoker(dict(elms))
    assert sorted(c.return_extremes()) == sorted(["Mauricio", "Frank"])
