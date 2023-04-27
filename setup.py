#!/usr/bin/env python


import codecs

from setuptools import setup

with codecs.open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    author='Joneai',
    author_email='mxjoneai@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
    ],
    description='Django CAS 1.0/2.0/3.0 client authentication library, support Django 2.2, 3.0, 3.1, 3.2, 4.0 and Python 3.7+',
    keywords=['django', 'cas', 'cas2', 'cas3', 'client', 'sso', 'single sign-on', 'Central Authentication Service', 'authentication', 'auth'],
    license='BSD',
    long_description=readme,
    name='django-cas-nge',
    packages=['django_cas_ng', 'django_cas_ng.management', 'django_cas_ng.management.commands', 'django_cas_ng.migrations'],
    package_data={
        'django_cas_ng': [
            'locale/*/LC_MESSAGES/*',
            'py.typed',
        ],
    },
    url='https://djangocas.dev',
    download_url='https://github.com/tacnaci/django-cas-nge/releases',
    version='4.3.3',
    python_requires=">=3.7",
    install_requires=[
        'Django>=2.2',
        'python-cas>=1.6.0',
    ],
    zip_safe=False,  # dot not package as egg or django will not found management commands
)
