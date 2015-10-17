from setuptools import setup, find_packages
__author__ = 'Atsushi Odagiri'
__version__ = "0.1"


requires = [
    "pyramid",
    "pyramid_tm",
    "pyramid_jinja2",
    "pyramid_sqlalchemy",
    "pyramid_deform",
    "pyramid_layout",
    "deform>=2.0dev",
    "colanderalchemy",
]

tests_require = [
    "pytest",
    "pytest-cov",
    "testfixtures",
    "webtest",
]

dev_requires = tests_require + [
    "psycopg2",
    "waitress",
    "pyramid_debugtoolbar",
    "alembic",
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
    tests_require=tests_require,
    extras_require={
        "dev": dev_requires,
        "testing": tests_require,
    },
    entry_points=points,
)
