
from setuptools import setup, find_packages

setup(
    name="Rubato",
    version="0.1",
    packages=find_packages(),
    test_suite="test",
    install_requires=[
        "django",
        "django-allauth",
        "slacker",
        "websocket-client",
    ],
)

