from __future__ import annotations

from django.core.management.base import BaseCommand
from example.core.models import Book


class Command(BaseCommand):
    help = "List all books"

    def handle(self, *args: object, **options: object) -> None:
        # TODO: add profiling just around this block
        # with cProfile.Profile() as profiler:
        self.print_books()

        # profiler.dump_stats("profile.pstats")

    def print_books(self) -> None:
        books = Book.objects.order_by("title")
        for book in books:
            print(book.title, "by", book.author.name)
