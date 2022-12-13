from builder.builder import Builder
from model.set_advice import SetAdviceModel
from model.set import SetModel


class SetAdviceBuilder(Builder):

    def __init__(self, values: dict):
        super().__init__(values)
        self.set_advice = SetAdviceModel.from_dict(values)

    def set_set(self, set: SetModel):
        self.set_advice.set = set
        return self

    def populate(self) -> SetAdviceModel:
        return self.set_advice
