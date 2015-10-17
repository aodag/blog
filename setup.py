from setuptools import setup, find_packages
__author__ = 'Atsushi Odagiri'
__version__ = "0.1"


requires = [
    "pyramid",
    "pyramid_tm",
    "pyramid_jinja2",
    "pyramid_sqlalchemy",
    "deform>=2.0dev",
    "colanderalchemy",
]

dev_requires = [
    "psycopg2",
    "waitress",
    "pyramid_debugtoolbar",
]

points = {
    "paste.app_factory": [
        "main=blog:main",
    ],
}

setup(
    name="blog",
    version=__version__,
    author=__author__,
    author_email="aodagx@gmail.com",
    packages=find_packages(),
    install_requires=requires,
    extras_require={
        "dev": dev_requires,
    },
    entry_points=points,
)
