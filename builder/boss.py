from typing import List

from builder.builder import Builder
from model.boss import BossModel
from model.tactic import TacticModel


class BossBuilder(Builder):

    def __init__(self, values: dict):
        super().__init__(values)
        self.boss = BossModel.from_dict(values)

    def set_tactic(self, tactic: TacticModel):
        self.boss.tactic = tactic
        return self

    def populate(self) -> BossModel:
        return self.boss
