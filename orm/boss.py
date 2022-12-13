import json

from orm.orm import DAL


class BossDAL(DAL):
    model = 'boss'
    file = 'bosses/other.json'
    per_trial = [
        'bosses/hrc.json',
        'bosses/aa.json',
        'bosses/so.json',
        'bosses/mol.json',
        'bosses/hof.json',
        'bosses/as.json',
        'bosses/cr.json',
        'bosses/ss.json',
        'bosses/ka.json',
        'bosses/rg.json',
        'bosses/dsr.json',
    ]

    def __init__(self):
        super().__init__()
        for file in self.per_trial:
            src = f'{self.base}/{file}'
            with open(src) as f:
                self.data.update(json.loads(f.read()))
