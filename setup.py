from setuptools import setup

setup(
    name='fastapi',
    version='0.1.0',
    description='FastAPI boilerplate',
    author='lynnetsy',
    author_email='lyncelgarros@gmail.com',
    packages=['app'],
    python_requires='>=3.11',
    install_requires=[],
    extras_requires={
        'dev': [],
    }
)