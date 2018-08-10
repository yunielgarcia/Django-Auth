from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreateForm
from django.views import generic
from django.core.urlresolvers import reverse_lazy


class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy("posts:all")
    template_name = "accounts/login.html"

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class LogoutView(generic.RedirectView):
    url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)



class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'