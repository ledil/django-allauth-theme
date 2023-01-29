# -*- coding: utf-8 -*-
from django.conf import settings


class AppSettings(object):
    @property
    def DAT_WELCOME_TITLE(self):
        return getattr(settings, "DAT_WELCOME_TITLE", "Welcome")

    @property
    def DAT_WELCOME_TITLE_MOBILE(self):
        return getattr(settings, "DAT_WELCOME_TITLE_MOBILE", "Welcome mobile")

    @property
    def DAT_GOOGLE_ENABLE_ONETAP_LOGIN(self):
        return getattr(settings, "DAT_GOOGLE_ENABLE_ONETAP_LOGIN", False)

    @property
    def DAT_GOOGLE_CLIENT_ID(self):
        return getattr(settings, "DAT_GOOGLE_CLIENT_ID", "google_client_id")

    @property
    def DAT_BASE_URL(self):
        return getattr(settings, "DAT_BASE_URL", "http://localhost:8000")

    @property
    def DAT_WELCOME_TEXT(self):
        return getattr(settings, "DAT_WELCOME_TEXT",
                       "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor"
                       " invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua")
