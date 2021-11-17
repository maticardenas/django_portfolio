from typing import TYPE_CHECKING
from django.shortcuts import render
from projects.models import Project

if TYPE_CHECKING:
    from response import Response
    from urllib.request import Request

def project_index(request: "Request") -> "Response":
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request: "Request", pk: int) -> "Response":
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)