# -*- coding: utf-8 -*-
from .app_settings import AppSettings


def welcome_text(request):
    conf = AppSettings()
    return {
        'DAT_WELCOME_TITLE': conf.DAT_WELCOME_TITLE,
        'DAT_WELCOME_TITLE_MOBILE': conf.DAT_WELCOME_TITLE_MOBILE,
        'DAT_WELCOME_TEXT': conf.DAT_WELCOME_TEXT,
        'DAT_GOOGLE_ENABLE_ONETAP_LOGIN': conf.DAT_GOOGLE_ENABLE_ONETAP_LOGIN,
        'DAT_GOOGLE_CLIENT_ID': conf.DAT_GOOGLE_CLIENT_ID,
        'DAT_BASE_URL': conf.DAT_BASE_URL
    }
