## Check benchmark your functions while unit testing them

Usecases:
1. Problem solving
2. Quick algorithm mockup


```Python
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
```

```Bash
test_function_a (__main__.TestSrc): 0:00:00.000052
.
test_function_b (__main__.TestSrc): 0:00:01.001192
.
----------------------------------------------------------------------
Ran 2 tests in 1.002s

OK
```
