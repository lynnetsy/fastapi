from setuptools import setup

setup(
    name='fastapi',
    version='0.1.0',
    description='FastAPI boilerplate',
    author='lynnetsy',
    author_email='lyncelgarros@gmail.com',
    packages=['app'],
    python_requires='>=3.11',
    install_requires=[
        "asyncpg==0.28.0",
        "loguru==0.7.2",
        "sqlalchemy==2.0.22",
    ],
    extras_requires={
        'dev': [],
    }
)