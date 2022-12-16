import json
from typing import List


class Config:

    instance = None

    config_path = 'src/config.json'
    secret_path = 'src/secret.json'

    bosses_src: List[str]
    trials_src: List[str]
    sets_src: List[str]
    help_src: str
    token: str

    def __init__(self):
        if Config.instance:
            raise Exception('Config already exists')
        with open(self.config_path) as f:
            config = json.loads(f.read())
        with open(self.secret_path) as f:
            secret = json.loads(f.read())
        self.bosses_src = config.get('bosses_src', [])
        self.trials_src = config.get('trials_src', [])
        self.sets_src = config.get('sets_src', [])
        self.help_src = config.get('help_src', [])
        self.token = secret.get('token', '')
        Config.instance = self

    @classmethod
    def get(cls):
        if Config.instance:
            return Config.instance
        else:
            return Config()
