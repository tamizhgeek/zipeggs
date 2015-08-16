from setuptools import setup

setup(
    name = "zipeggs",
    entry_points = {'zc.buildout': ['zipeggs = zipeggs:ZipEggs']},
    py_modules=['zipeggs'],
    version="0.1"
    )
