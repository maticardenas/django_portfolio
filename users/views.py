from typing import TYPE_CHECKING

from django.shortcuts import render

if TYPE_CHECKING:
    from response import Response
    from urllib.request import Request


def dashboard(request: "Request") -> "Response":
    return render(request, "dashboard.html")