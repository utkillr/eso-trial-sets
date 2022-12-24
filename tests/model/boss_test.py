import pytest

from model.boss import BossModel


def _default_data():
    return {
        'id': 'test-id',
        'name': 'test-name',
        'description': 'test-description',
    }


def _default_test(boss: BossModel):
    assert boss.id == 'test-id'
    assert boss.name == 'test-name'
    assert boss.description == 'test-description'


def test_boss_model_min():
    data = _default_data()
    boss = BossModel.from_dict(data)
    _default_test(boss)
    assert boss.tactic is None
    assert len(boss.links) == 0


def test_boss_model_max():
    data = _default_data()
    tactic = ['a', 'b', 'c']
    links = ['1', '2', '3']
    data['tactic'] = tactic
    data['links'] = links
    boss = BossModel.from_dict(data)
    _default_test(boss)
    assert boss.tactic == tactic
    assert boss.links == links


def test_boss_model_miss():
    data = _default_data()
    del data['id']
    with pytest.raises(ValueError):
        BossModel.from_dict(data)


def test_boss_model_extra():
    data = _default_data()
    data['eh'] = 'eh'
    boss = BossModel.from_dict(data)
    _default_test(boss)
