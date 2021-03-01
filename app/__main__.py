import random
import sys

from app.config import SPINNERS_DICT
from app.utils import print_spinner_frames

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        iterations = 5
    else:
        try:
            iterations = int(sys.argv[1])
        except Exception:
            raise ValueError(f"Please enter a valid integer for the iterations. {e}")

    spinner = random.choice(list(SPINNERS_DICT.keys()))

    name = spinner
    frames = SPINNERS_DICT[name]["frames"]
    interval = SPINNERS_DICT[name]["interval"]

    print_spinner_frames(frames, interval, name, iterations=iterations)
    print('\n')
