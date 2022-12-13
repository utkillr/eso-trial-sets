from config.config import Config
from orm.orm import DAL


class TrialDAL(DAL):
    model = 'trial'
    src = Config.get().trials_src
