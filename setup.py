import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("logger/__init__.py", "r") as file:
    regex_version = r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]'
    version = re.search(regex_version, file.read(), re.MULTILINE).group(1)

with open("README.md", "rb") as file:
    readme = file.read().decode("utf-8")

setup(
    name="logger",
    version=version,
    packages=["logger"],
    description="Python logging made (stupidly) simple",
    long_description=readme,
    author="Delgan",
    author_email="sagarborse90@gmail.com",
    url="https://github.com/sagarborse/logger",
    download_url="https://github.com/sagarborse/logger/archive/{}.tar.gz".format(version),
    keywords=["logging", "logger", "log", "parser"],
    license="MIT license",
    install_requires=[
        "django-structlog==1.2.3",
        "colorama"
    ],
    python_requires=">=3.5",
)
