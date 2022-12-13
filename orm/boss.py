from config.config import Config
from orm.orm import DAL


class BossDAL(DAL):
    model = 'boss'
    src = Config.get().bosses_src
