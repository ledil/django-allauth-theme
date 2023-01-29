from django.urls import path, include, re_path
from django.views.defaults import page_not_found
from django.views.decorators.csrf import csrf_exempt

from .views import CustomSignupView, CustomLoginView, CustomLogoutView, CustomPasswordSetView, \
    CustomPasswordChangeView, CustomEmailVerificationSentView, CustomConfirmEmailView, CustomAccountInactiveView, \
    CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetFromKeyView, \
    CustomPasswordResetFromKeyDoneView, CustomGoogleOneTapView

urlpatterns = [
    path("accounts/google_onetap_login/", csrf_exempt(CustomGoogleOneTapView.as_view()), name="account_google_onetap_login"),
    path("accounts/signup/", CustomSignupView.as_view(), name="account_signup"),
    path("accounts/email/", page_not_found, kwargs={"exception": Exception("Page not Found")}),
    path("accounts/login/", CustomLoginView.as_view(), name="account_login"),
    path("accounts/logout/", CustomLogoutView.as_view(), name="account_logout"),
    path("accounts/password/change/", CustomPasswordChangeView.as_view(), name="account_change_password"),
    path("accounts/password/set/", CustomPasswordSetView.as_view(), name="account_set_password"),
    path("accounts/inactive/", CustomAccountInactiveView.as_view(), name="account_inactive"),
    path("accounts/confirm-email/", CustomEmailVerificationSentView.as_view(), name="account_email_verification_sent"),
    re_path(r"^accounts/confirm-email/(?P<key>[-:\w]+)/$", CustomConfirmEmailView.as_view(),
            name="account_confirm_email"),
    path("accounts/password/reset/", CustomPasswordResetView.as_view(), name="account_reset_password"),
    path("accounts/password/reset/done/", CustomPasswordResetDoneView.as_view(), name="account_reset_password_done"),
    re_path(r"^accounts/password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
            CustomPasswordResetFromKeyView.as_view(), name="account_reset_password_from_key"),
    path("accounts/password/reset/key/done/", CustomPasswordResetFromKeyDoneView.as_view(),
         name="account_reset_password_from_key_done"),
    path('accounts/', include('allauth.urls')),
]
