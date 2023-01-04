import json
from pathlib import Path
from datetime import datetime

from config.config import Config


def save_suggest(user: str, trial: str, boss: str, role: str, set: str, why: str):
    path = Path(Config.get().suggest_src)
    path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d')
    file = f'{path}/{user}_{timestamp}.json'

    if Path(file).is_file():
        with open(file, 'r') as f:
            suggestion = json.loads(f.read())
    else:
        suggestion = {}

    if trial not in suggestion:
        suggestion[trial] = {}

    if boss not in suggestion[trial]:
        suggestion[trial][boss] = {}

    if role not in suggestion[trial][boss]:
        suggestion[trial][boss][role] = []

    suggestion[trial][boss][role].append(
        {
            'set': set,
            'why': why,
        }
    )

    with open(file, 'w') as f:
        f.write(json.dumps(suggestion, indent=4))
