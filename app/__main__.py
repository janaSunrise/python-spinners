import random

from app.config import SPINNERS_DICT
from app.utils import print_spinner_frames

if __name__ == '__main__':
    spinner = random.choice(list(SPINNERS_DICT.keys()))

    name = spinner
    frames = SPINNERS_DICT[name]["frames"]
    interval = SPINNERS_DICT[name]["interval"]

    print_spinner_frames(frames, interval, name)
    print('\n')
