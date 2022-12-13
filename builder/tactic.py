from typing import List

from builder.builder import Builder
from model.tactic import TacticModel
from model.set_advice import SetAdviceModel


class TacticBuilder(Builder):

    def __init__(self, values: dict):
        super().__init__(values)
        self.tactic = TacticModel.from_dict(values)

    def set_set_advices(self, set_advices: List[SetAdviceModel]):
        self.tactic.sets = set_advices
        return self

    def set_set_prohibitions(self, set_advices: List[SetAdviceModel]):
        self.tactic.no_sets = set_advices
        return self

    def populate(self) -> SetAdviceModel:
        return self.tactic
