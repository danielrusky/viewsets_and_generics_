from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from users.models import User




