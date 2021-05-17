from __future__ import annotations

import socket
import time
from queue import Queue
from threading import Thread

timeout = 1.0


def check_port(host: str, port: int, results: Queue[int]) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))
    sock.close()
    if result == 0:
        results.put(port)


def main() -> None:
    start = time.perf_counter_ns()
    host = "adamj.eu"
    threads = []
    results: Queue[int] = Queue()
    # TODO: scan less + more ports (safe range: 80-500), and see how runtime
    # changes.
    for port in range(440, 450):
        t = Thread(target=check_port, args=(host, port, results))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    while not results.empty():
        port = results.get()
        print(f"Port {port} is open")

    duration = (time.perf_counter_ns() - start) / 1e9
    print(f"Completed scan in {duration} seconds")


if __name__ == "__main__":
    main()
