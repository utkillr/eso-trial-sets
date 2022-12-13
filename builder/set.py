from builder.builder import Builder
from model.set import SetModel


class SetBuilder(Builder):

    def __init__(self, values: dict):
        super().__init__(values)
        self.set = SetModel.from_dict(values)

    def populate(self) -> SetModel:
        return self.set
