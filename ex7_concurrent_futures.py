from __future__ import annotations

import socket
import time
from concurrent.futures import ThreadPoolExecutor

timeout = 1.0


def check_port(host: str, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0


def main() -> None:
    host = "adamj.eu"

    start = time.perf_counter_ns()
    with ThreadPoolExecutor() as executor:
        future_to_port = {
            executor.submit(check_port, host, port): port for port in range(440, 450)
        }
        # TODO: finish based on documentation example:
        # https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor-example  # noqa: B950
        future_to_port
    duration = (time.perf_counter_ns() - start) / 1e9
    print(f"Completed scan in {duration} seconds")

    # TODO: repeat with ProcessPoolExecutor to measure difference in timing


if __name__ == "__main__":
    main()
