from setuptools import setup

setup(
    install_requires = (
        'Flask',
        'sqlalchemy',
        'feedparser',
        'PyMySQL',
        'cachetools',
        'Flask-Cors'
    )
)