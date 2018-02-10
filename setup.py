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
    version="1.0.1",
    description="Zip flattened out eggs back again",
    long_description="Buildout when collecting eggs, always flattens out the eggs as directories. We had a requirement where the eggs are needed as zips not as dirs. So this recipe. This will take a folder as input, iterate through the folders in it and create zip archives out of all folders inside it.",
    url="https://github.com/tamizhgeek/zipeggs",
    author="Azhagu Selvan",
    license="Apache 2.0"
)
