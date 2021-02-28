import random

from app.config import SPINNERS_DICT
from app.utils import print_spinner_frames

if __name__ == '__main__':
    spinner = random.choice(SPINNERS_DICT)

    name = spinner["name"]
    frames = spinner["frames"]
    interval = spinner["interval"]

    print_spinner_frames(frames, interval, name)
    print('\n')
