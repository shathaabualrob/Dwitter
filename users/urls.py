from django.urls import include, path
from users.views import guest_dashboard, register

app_name = "users"
urlpatterns = [
    path("", include('dwitter.urls')),
    # path('dashboard/', dashboard, name="dashboard"),
    path("", guest_dashboard, name="guest_dashboard"),
    path('accounts/', include("django.contrib.auth.urls")),
    path("register/", register, name="register"),
]
