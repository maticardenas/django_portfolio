from django.contrib.auth import login
from django.urls import reverse
from typing import TYPE_CHECKING

from django.shortcuts import render, redirect

from users.forms import CustomUserCreationForm

if TYPE_CHECKING:
    from response import Response
    from urllib.request import Request


def dashboard(request: "Request") -> "Response":
    return render(request, "dashboard.html")


def register(request: "Request") -> "Response":
    if request.method == "GET":
        return render(
            request, "register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            login(request, user)
            return redirect(reverse("dashboard"))