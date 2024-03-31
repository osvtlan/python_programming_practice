import time


def mean(calls_to_count: int):
    def inner_mean(func):
        latest_calls_time = []

        def inner(*args, **kwargs):
            start_ts = time.time()
            res = func(*args, **kwargs)
            end_ts = time.time()
            call_time = end_ts - start_ts
            latest_calls_time.append(call_time)
            if len(latest_calls_time) > calls_to_count:
                latest_calls_time.pop(0)
            average_time = sum(latest_calls_time) / len(latest_calls_time)
            print(
                f"Average execution time of the last {len(latest_calls_time)} function calls - {average_time:.5f}"
            )
            return res

        return inner

    return inner_mean


@mean(10)
def foo(arg1):
    pass


@mean(2)
def boo(arg1):
    pass


if __name__ == "__main__":
    for _ in range(100):
        foo("Walter")
