# django-allauth-theme

An awesome and responsive django-allauth theme based on tailwind.

<img width="700" alt="screenshot_login" src="https://github.com/ledil/django-allauth-theme/assets/64521/9b9ff7e4-514c-4484-b2c3-d4a611e95503">


## Install

```bash
pip install django-allauth-theme
```

### Configuring the settings file

First of all, add `allauth_theme` and `crispy_forms` to `INSTALLED_APPS`.

```python
INSTALLED_APPS = (
  ...
  'crispy_forms',
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

Now include the urls in your urls.py

```python
urlpatterns = [
    ...
    path('', include('allauth_theme.urls')),
    ...
]
```

Configuration for settings:

```python
DAT_WELCOME_TITLE = 'Welcome Title'  # title
DAT_WELCOME_TITLE_MOBILE = 'Welcome mobile'  # mobile title
DAT_WELCOME_TEXT = 'Description of your project'  # text for your project
DAT_GOOGLE_ENABLE_ONETAP_LOGIN = True  # decide if you want to show the google one tap login
DAT_GOOGLE_CLIENT_ID = ''  # google client id , e.g. XXXXXXXXXX39-62ckbbeXXXXXXXXXXXXXXXXXXXXXm1.apps.googleusercontent.com
DAT_BASE_URL = ''  # e.g. http://localhost:8000
DAT_TOS_MESSAGE = 'By registering, you agree to our <a href="">Terms of Service</a> and <a href="">Privacy Policy.</a>'  # optional
```

### Google One Tap Login

If you want to use the google one tap you must you must include following changes to your settings for developement environment:

#### Some notices for the developing environment

```python
SECURE_REFERRER_POLICY = 'no-referrer-when-downgrade'
```

Add http://localhost, http://localhost:8000, http://127.0.0.1 and http://127.0.0.1:8000 to your "Authorized JavaScript origins" in your google developer console. While you are working in the development environment you must use "localhost" instead of "127.0.0.1". As "Authorized redirect URIs" just use following URIs if you are working in the development environment:

```http://localhost:8000/accounts/google/login/callback/```


You can add also use 127.0.0.1 as URI if you don't want to use Google One Tap functionally while developing.
