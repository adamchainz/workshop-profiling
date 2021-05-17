from __future__ import annotations

import asyncio
import socket
import time

timeout = 1.0


async def check_port(host: str, port: int, results: list[int]) -> None:
    try:
        future = asyncio.open_connection(host=host, port=port)
        read, write = await asyncio.wait_for(future, timeout=timeout)
        results.append(port)
        write.close()
    except OSError:
        # pass on port closure
        pass
    except asyncio.TimeoutError:
        # Port is closed, skip and continue
        pass


async def check_port_badly(host: str, port: int, results: list[int]) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))
    sock.close()
    if result == 0:
        results.append(port)


async def main() -> None:
    start = time.perf_counter_ns()
    host = "adamj.eu"

    results: list[int] = []
    # TODO:
    # 1. run with check_port_badly() in Python dev mode
    # 2. switch to check_port()
    # 3. scan less + more ports (safe range: 80-500), and see how runtime
    #    changes.
    tasks = [check_port_badly(host, port, results) for port in range(440, 550)]
    await asyncio.gather(*tasks)

    for port in results:
        print(f"Port {port} is open")

    duration = (time.perf_counter_ns() - start) / 1e9
    print(f"Completed scan in {duration} seconds")


if __name__ == "__main__":
    asyncio.run(main())
