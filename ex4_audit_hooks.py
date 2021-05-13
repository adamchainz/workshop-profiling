# Our mini-profiler

from __future__ import annotations

import sys
import time

# Our mini-profiler

last_import_module: str | None = None
last_import_now: int | None = None


def log_import_audit_hook(event: str, args: tuple[str, ...]) -> None:
    global last_import_module, last_import_now
    if event != "import":
        return

    # Arguments documented at: https://docs.python.org/3/library/audit_events.html
    module, *_unused = args
    now = time.perf_counter_ns()

    # Log previous import
    if last_import_module is not None:
        duration = (now - last_import_now) / 1e9
        # TODO: ignore module names beginning with "_"
        print(f"{last_import_module}: {duration:.4f}s")

    # Store current import
    last_import_module = module
    last_import_now = now


if __name__ == "__main__":
    sys.addaudithook(log_import_audit_hook)

# Our app’s imports

import datetime  # noqa
import html.parser  # noqa
import json  # noqa

# Show final import

if __name__ == "__main__":
    log_import_audit_hook("import", ("dummy",))
