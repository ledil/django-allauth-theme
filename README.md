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