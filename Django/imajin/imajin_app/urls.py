from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.sign_up, name="signup"),
    path("login/", views.log_in, name="login"),
    path("coming/", views.coming_soon, name="coming"),
    path("contact/", views.contact_us, name="contact"),
]