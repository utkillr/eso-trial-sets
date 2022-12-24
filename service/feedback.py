from pathlib import Path
from datetime import datetime

from config.config import Config


def save_feedback(user: str, message: str):
    path = Path(Config.get().feedback_src)
    path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    file = f'{user}_{timestamp}'

    with open(f'{path}/{file}.txt', 'w') as f:
        f.write(message)
