import pytest

from model.tactic import TacticModel


def test_tactic_model_min():
    TacticModel.from_dict({})


def test_tactic_model_max():
    sets = ['a', 'b', 'c']
    no_sets = ['1', '2', '3']
    data = {
        'sets': sets,
        'no_sets': no_sets,
    }
    tactic = TacticModel.from_dict(data)
    assert tactic.sets == sets
    assert tactic.no_sets == no_sets


def test_set_model_extra():
    data = {'eh': 'eh'}
    TacticModel.from_dict(data)
