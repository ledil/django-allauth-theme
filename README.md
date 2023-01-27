# django-allauth-theme

An awesome django-allauth theme based on tailwind.

## Install

```bash
pip install django-allauth-theme
```

### Configuring the settings file

First of all, add `allauth_theme` to `INSTALLED_APPS`.

```python
INSTALLED_APPS = (
  ...
  'allauth_theme',
  ...
)
```

Add following context processors to the list:

```python
TEMPLATES = [
 {
   ...
   'OPTIONS': {
      'context_processors': [
        ...
        'allauth_theme.context_processors.welcome_text'
   ],
  }
 }
]
```

Configuration for settings:

```python
DAT_WELCOME_TITLE = 'Welcome Title'  # title
DAT_WELCOME_TITLE_MOBILE = 'Welcome mobile'  # mobile title
DAT_WELCOME_TEXT = 'Description of your project'  # text for your project
DAT_GOOGLE_ENABLE_ONETAP_LOGIN = True  # decide if you want to show the google one tap login
DAT_GOOGLE_CLIENT_ID = ''  # google client id 
```