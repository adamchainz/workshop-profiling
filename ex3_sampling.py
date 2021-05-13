from __future__ import annotations

import sys
import threading
import time


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


def profiler() -> None:
    main_thread_id = threading.main_thread().ident
    assert main_thread_id is not None
    start = time.perf_counter_ns()

    while True:
        time.sleep(0.1)

        frame = sys._current_frames()[main_thread_id]
        duration = (time.perf_counter_ns() - start) / 1e9

        # TODO: print caller function name too
        function_name = frame.f_code.co_name
        del frame
        print(f"{function_name}(): {duration:.4f}s")


# Call app with profiler running

if __name__ == "__main__":
    thread = threading.Thread(target=profiler, daemon=True)
    thread.start()

    main()
