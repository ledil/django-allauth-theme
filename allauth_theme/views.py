from allauth.account.views import SignupView, LoginView, LogoutView, PasswordSetView, PasswordChangeView, \
    ConfirmEmailView, EmailVerificationSentView, AccountInactiveView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetFromKeyView, PasswordResetFromKeyDoneView
from allauth.decorators import rate_limit
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic import RedirectView

from .forms import CustomSignupForm


@method_decorator(rate_limit(action="signup"), name="dispatch")
class CustomSignupView(SignupView):
    form_class = CustomSignupForm
    template_name = 'allauth/account/signup.html'


class CustomLoginView(LoginView):
    template_name = 'allauth/account/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'allauth/account/logout.html'


class CustomGoogleOneTapView(RedirectView):
    def get_redirect_url(self, **kwargs):
        return '/accounts/google/login/'

@method_decorator(
    # NOTE: 'change_password' (iso 'set_') is intentional, there is no need to
    # differentiate between set and change.
    rate_limit(action="change_password"),
    name="dispatch",
)
class CustomPasswordSetView(LoginRequiredMixin, PasswordSetView):
    template_name = 'allauth/account/password_set.html'


@method_decorator(rate_limit(action="change_password"), name="dispatch")
class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'allauth/account/password_change.html'


class CustomEmailVerificationSentView(EmailVerificationSentView):
    template_name = "allauth/account/verification_sent.html"


class CustomConfirmEmailView(ConfirmEmailView):
    template_name = "allauth/account/email_confirm.html"


class CustomAccountInactiveView(AccountInactiveView):
    template_name = "allauth/account/account_inactive.html"


@method_decorator(rate_limit(action="reset_password"), name="dispatch")
class CustomPasswordResetView(PasswordResetView):
    template_name = "allauth/account/password_reset.html"


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "allauth/account/password_reset_done.html"


@method_decorator(rate_limit(action="reset_password_from_key"), name="dispatch")
class CustomPasswordResetFromKeyView(PasswordResetFromKeyView):
    template_name = 'allauth/account/password_reset_from_key.html'


class CustomPasswordResetFromKeyDoneView(PasswordResetFromKeyDoneView):
    template_name = "allauth/account/password_reset_from_key_done.html"
