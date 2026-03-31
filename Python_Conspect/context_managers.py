import time
from contextlib import contextmanager


class MeasureTime:
    def __init__(self, msg_pref):
        self.msg = msg_pref

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, trackback):
        self.end = time.perf_counter()
        print(f'{self.msg}: elapsed time {(self.end - self.start) * 1000:.2f} ms')
        return False


@contextmanager
def measure_time(msg):
    start = time.perf_counter()
    try:
        yield start
    finally:
        end = time.perf_counter()
        print(f'{msg}: elapsed time {(end - start) * 1000:.2f} ms')


with MeasureTime('op1'):
    time.sleep(0.1)

with measure_time('op2'):
    time.sleep(0.2)


@measure_time('op3')
def test():
    time.sleep(0.15)


test()
