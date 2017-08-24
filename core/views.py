from django.shortcuts import render
from django.views.generic import FormView, ListView
from .forms import GenerateRandomUsersForm
from .tasks import create_random_user_accounts
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages

class GenerateRandomUsersView(FormView):
    template_name = 'generate_random_users.html'
    form_class = GenerateRandomUsersForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your' \
            ' random users! Wait a moment and refresh this page.')
        return redirect('users_list')


class UserListView(ListView):
    model = User
    template_name = 'users_list.html'



