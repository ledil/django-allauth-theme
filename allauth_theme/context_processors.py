# -*- coding: utf-8 -*-
from .app_settings import AppSettings


def welcome_text(request):
    conf = AppSettings()
    return {
        'DAT_WELCOME_TITLE': conf.DAT_WELCOME_TITLE,
        'DAT_WELCOME_TITLE_MOBILE': conf.DAT_WELCOME_TITLE_MOBILE,
        'DAT_WELCOME_TEXT': conf.DAT_WELCOME_TEXT,
    }
