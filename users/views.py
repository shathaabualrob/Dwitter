from django.shortcuts import redirect,render
from django.urls import reverse
from django.contrib.auth import login
from users.forms import CustomUserCreationForm


# Create your views here.
def guest_dashboard(request):
    return render(request, "guest_dashboard.html")
def register(request):
    return render(request, "register.html")
def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))