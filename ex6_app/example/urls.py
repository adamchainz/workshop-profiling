from __future__ import annotations

import debug_toolbar
from django.urls import path, include

from example.core import views

urlpatterns = [
    path("", views.index),
    path("__debug__/", include(debug_toolbar.urls)),
]
