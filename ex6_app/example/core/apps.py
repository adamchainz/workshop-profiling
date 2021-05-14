from __future__ import annotations

import time

from django.db import connections
from django.db.backends.signals import connection_created


def make_queries_slower(execute, sql, params, many, context):
    # Slow down queries to simulate databases slower than SQLite
    time.sleep(0.001)
    return execute(sql, params, many, context)


def install_make_queries_slower(connection, **kwargs):
    if make_queries_slower not in connection.execute_wrappers:
        connection.execute_wrappers.append(make_queries_slower)


connection_created.connect(install_make_queries_slower)
for connection in connections.all():
    install_make_queries_slower(connection=connection)
