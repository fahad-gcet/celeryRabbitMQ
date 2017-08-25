from django.shortcuts import render
from django.views.generic import FormView, ListView
from .forms import GenerateRandomUsersForm, SendMailForm
from .tasks import create_random_user_accounts, send_email
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail

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
    user_count = 0

    def get_context_data(self, **kwargs):
        self.user_count = User.objects.all().count()
        context = super(UserListView, self).get_context_data(**kwargs)
        context.update({'user_count': self.user_count})
        return context


class SendMailView(FormView):
    template_name = 'send_mail.html'
    form_class = SendMailForm

    def form_valid(self, form):
        to = form.cleaned_data.get('to')
        subject = form.cleaned_data.get('subject')
        body = form.cleaned_data.get('body')
        send_mail(subject, body, 'noreply@celeryRabbit.me' ,[to,])
        messages.success(self.request, 'Email has been sent')
        return redirect('users_list')


class SendMailCeleryView(FormView):
    template_name = 'send_mail.html'
    form_class = SendMailForm

    def form_valid(self, form):
        to = form.cleaned_data.get('to')
        subject = form.cleaned_data.get('subject')
        body = form.cleaned_data.get('body')
        send_email.delay(to, subject, body)
        messages.success(self.request, 'Email has been sent')
        return redirect('users_list')



