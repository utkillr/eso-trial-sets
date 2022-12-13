from model.model import Model


class TacticModel(Model):

    def __init__(self, sets=None, no_sets=None):
        super().__init__()
        self.sets = sets
        self.no_sets = no_sets

    @classmethod
    def from_dict(cls, values):
        return TacticModel()
