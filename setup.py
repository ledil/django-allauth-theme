from setuptools import setup, find_packages

version = __import__("allauth_theme").__version__

setup(
   name='django-allauth-theme',
   version=version,
   author='Leonardo Di Lella',
   author_email='leonardo.dilella@mobileapart.com',
   packages=find_packages(),
   keywords="django auth account social openid twitter facebook oauth registration theme tailwindcss",
   url='http://pypi.python.org/pypi/django-allauth-theme/',
   license='LICENSE',
   description='An Awesome django-allauth theme based on tailwind',
   long_description_content_type="text/markdown",
   long_description=open('README.md').read(),
   install_requires=[
        "Django >= 2.0",
        "django-allauth >= 0.51.0"
    ],
    python_requires=">=3.5",
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
        "Topic :: Internet",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
   ]
)
