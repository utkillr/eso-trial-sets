from config.config import Config
from orm.orm import DAL


class SetDAL(DAL):
    model = 'set'
    src = Config.get().sets_src
