from __future__ import annotations

import sys
import time
from types import FrameType


# Our app


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


# Our mini-profiler

starts = []


def tracer(frame: FrameType, event: str, arg: object) -> None:
    if event in "call":
        starts.append(time.perf_counter_ns())

    elif event == "return":
        duration = (time.perf_counter_ns() - starts.pop()) / 1e9
        function_name = frame.f_code.co_name

        # TODO: ignore calls to log()
        print(f"{function_name}(): {duration:.04f}s")


# Call app with profiler

if __name__ == "__main__":
    sys.setprofile(tracer)
    main()
    sys.setprofile(None)
