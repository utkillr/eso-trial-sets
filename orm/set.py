import json

from orm.orm import DAL


class SetDAL(DAL):
    model = 'set'
    file = 'sets/other.json'
    per_trial = [
        'sets/craft.json',
        'sets/monster.json',
        'sets/relic.json',
        'sets/dungeon.json',
        'sets/trial.json',
    ]

    def __init__(self):
        super().__init__()
        for file in self.per_trial:
            src = f'{self.base}/{file}'
            with open(src) as f:
                self.data.update(json.loads(f.read()))
