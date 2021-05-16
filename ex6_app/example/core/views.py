from __future__ import annotations

from io import StringIO

from django.http import HttpRequest, HttpResponse

from example.core.models import Book


def index(request: HttpRequest) -> HttpResponse:
    output = StringIO()
    print("<html><body>", file=output)

    books = Book.objects.order_by("title")
    for book in books:
        print("<p>", book.title, "by", book.author.name, "</p>", file=output)

    print("</body></html>", file=output)

    return HttpResponse(output.getvalue())
