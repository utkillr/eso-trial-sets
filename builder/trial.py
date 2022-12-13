from typing import List

from builder.builder import Builder
from model.trial import TrialModel
from model.boss import BossModel


class TrialBuilder(Builder):

    def __init__(self, values: dict):
        super().__init__(values)
        self.trial = TrialModel.from_dict(values)

    def set_bosses(self, bosses: List[BossModel]):
        self.trial.bosses = bosses
        return self

    def populate(self) -> TrialModel:
        return self.trial
