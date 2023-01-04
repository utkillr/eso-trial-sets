from typing import List

from orm.set import SetDAL
from orm.trial import TrialDAL
from orm.boss import BossDAL

from builder.trial import TrialBuilder
from builder.boss import BossBuilder
from builder.tactic import TacticBuilder
from builder.set_advice import SetAdviceBuilder
from builder.set import SetBuilder

from model.set import SetModel
from model.trial import TrialModel
from model.boss import BossModel


class DataBase:

    instance = None

    def __init__(self):
        if DataBase.instance:
            raise Exception('Database instance already exists')
        else:
            self.trials = TrialDAL()
            self.sets = SetDAL()
            self.bosses = BossDAL()
            DataBase.instance = self

    @classmethod
    def get(cls):
        if DataBase.instance:
            return DataBase.instance
        else:
            return DataBase()

    def get_trials_only(self) -> List[TrialModel]:
        return [
            TrialBuilder(
                trial
            ).populate()
            for trial in self.trials.get_all()
        ]

    def get_trials_with_bosses(self) -> List[TrialModel]:
        return [
            TrialBuilder(
                trial
            ).set_bosses(
                [
                    BossBuilder(
                        self.bosses.get(boss_id)
                    ).populate()
                    for boss_id in trial.get('bosses', [])
                ]
            ).populate()
            for trial in self.trials.get_all()
        ]

    def _build_tactic(self, tactic: dict):
        return TacticBuilder(
            tactic
        ).set_set_advices(
            [
                SetAdviceBuilder(
                    set_advice
                ).set_set(
                    SetBuilder(
                        self.sets.get(set_advice.get('id'))
                    ).populate()
                ).populate()
                for set_advice in tactic.get('sets', [])
            ]
        ).set_set_prohibitions(
            [
                SetAdviceBuilder(
                    set_advice
                ).set_set(
                    SetBuilder(
                        self.sets.get(set_advice.get('id'))
                    ).populate()
                ).populate()
                for set_advice in tactic.get('no_sets', [])
            ]
        )

    def _build_boss(self, boss: dict, role: str) -> BossBuilder:
        return BossBuilder(
            boss
        ).set_tactic(
            self._build_tactic(
                boss.get('tactics').get(role)
            ).populate() if boss.get('tactics', {}).get(role) else None,
        )

    def get_trial(self, trial_id: str, role: str) -> TrialModel:
        trial = self.trials.get(trial_id)
        return TrialBuilder(
            trial
        ).set_bosses(
            [
                self._build_boss(
                    self.bosses.get(boss_id),
                    role,
                ).populate()
                for boss_id in trial.get('bosses', [])
            ]
        ).populate()

    def get_boss(self, boss_id: str, role: str) -> BossModel:
        boss = self.bosses.get(boss_id)
        return self._build_boss(
            boss,
            role,
        ).populate()

    def get_trial_bosses(self, trial_id: str) -> List[BossModel]:
        trial = self.trials.get(trial_id)
        return [
            BossBuilder(
                self.bosses.get(boss_id)
            ).populate()
            for boss_id in trial.get('bosses', [])
        ]

    def get_set(self, set_id: str) -> SetModel:
        set = self.sets.get(set_id)
        return SetBuilder(
            set
        ).populate()

    def get_sets(self) -> List[SetModel]:
        return [
            SetBuilder(
                set
            ).populate()
            for set in self.sets.get_all()
        ]
