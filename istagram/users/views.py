from django.views.generic import DetailView
from django.shortcuts import get_object_or_404

from .models import User

class ProfileDetailView(DetailView):
    model = User

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))
