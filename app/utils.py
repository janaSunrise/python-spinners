import codecs
import sys
import time

from app.config import CLEAR_LINE


def unicode_decode(text: str) -> str:
    try:
        return codecs.decode(text, "utf-8")
    except Exception:
        return text


def print_spinner_frames(frames, interval, name, iterations=5):
    for i in range(iterations):
        for frame in frames:
            frame = unicode_decode(frame)
            output = f"\r{frame} | {name}"
            sys.stdout.write(output)
            sys.stdout.write(CLEAR_LINE)
            sys.stdout.flush()
            time.sleep(0.001 * interval)
