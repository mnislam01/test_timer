import time

import test_timer


def function_a():
    ...


def function_b():
    time.sleep(1)


class TestSrc(test_timer.BenchTestCase):
    def test_function_a(self):
        function_a()

    def test_function_b(self):
        function_b()


if __name__ == "__main__":
    test_timer.main()
