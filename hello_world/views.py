from typing import TYPE_CHECKING

from django.shortcuts import render

if TYPE_CHECKING:
    from urllib.request import Request

def hello_world(request: "Request"):
    print(type(render(request, 'hello_world.html', {})))
    return render(request, 'hello_world.html', {})
