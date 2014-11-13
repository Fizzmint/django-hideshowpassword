from setuptools import setup, find_packages
import os

version = __import__('hideshowpassword').__version__
#version = "2.0"

install_requires = [
    'django',
]

setup(
    name = "django-hideshowpassword",
    version = version,
    url = 'http://github.com/fizzmint/django-hideshowpassword',
    license = 'BSD',
    platforms=['OS Independent'],
    description = "Integrate CloudFour's hideShowPassword on Django fields",
    author = "Colin Powell",
    author_email = 'colin@fizzmint.com',
    packages=find_packages(),
    install_requires = install_requires,
    include_package_data=True,
    zip_safe=False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    package_dir={
        'django-hideshowpassword': 'hideshowpassword',
    },
)
