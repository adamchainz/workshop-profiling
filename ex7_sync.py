from __future__ import annotations

import socket
import time

timeout = 1.0


def check_port(host: str, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0


def main() -> None:
    start = time.time()
    host = "adamj.eu"
    # TODO: scan less + more ports (safe range: 80-500), and see how runtime
    # changes.
    for port in range(440, 450):
        result = check_port(host, port)
        if result:
            print(f"Port {port} is open")

    print(f"Completed scan in {time.time() - start} seconds")


if __name__ == "__main__":
    main()
