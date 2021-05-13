from __future__ import annotations

import functools
import time
from collections.abc import Callable
from typing import Any, TypeVar, cast


# Our profiling

Func = TypeVar("Func", bound=Callable[..., Any])


def instrument(func: Func) -> Func:
    @functools.wraps(func)
    def wrapper(*args: object, **kwargs: object) -> object:
        start = time.perf_counter_ns()

        result = func(*args, **kwargs)

        # TODO: also print the number of allocated blocks with
        # sys.getallocatedblocks() before/after
        duration = (time.perf_counter_ns() - start) / 1e9
        print(f"{func.__name__}(): {duration:.4f}s")

        return result

    return cast(Func, wrapper)


time.sleep = instrument(time.sleep)


# Our app


@instrument
def main() -> None:
    log("Starting main()")
    pause(0.25)
    log("Doing maths")
    sum(range(100_000))
    log("Final operation")
    pause(0.5)


def log(message: str) -> None:
    # Imagine this sends the message to our logging system.
    pass


def pause(n: float) -> None:
    time.sleep(n)


main()
