from allauth.account.forms import SignupForm
from django.conf import settings
from django.forms import CheckboxInput, BooleanField
from django.utils.safestring import mark_safe


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hasattr(settings, 'DAT_TOS_MESSAGE'):
            self.fields["tos"] = BooleanField(
                label=mark_safe(settings.DAT_TOS_MESSAGE),
                widget=CheckboxInput(attrs={'class': 'text-gray-700 text-sm signup_tos_checkbox'}), required=True
            )
