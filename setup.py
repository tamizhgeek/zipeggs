from setuptools import setup

setup(
    name="zipeggs",
    entry_points={
        'zc.buildout': [
            'default = zipeggs:ZipEggs',
            'zipeggs = zipeggs:ZipEggs',  # Legacy
        ],
    },
    py_modules=['zipeggs'],
    version="1.0"
)
