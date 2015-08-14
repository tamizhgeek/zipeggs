Zipeggs
-------

Buildout when collecting eggs, always flattens out the eggs as directories. We had a requirement where the eggs are needed as zips not as dirs. So this recipe.
This will take a folder as input, iterate through the folders in it and create zip archives out of all folders inside it.

Usage
-----

1. Add the recipe as zipeggs
2. Specify target=dir where you want the zipped eggs to be
3. Specify source=dir the directory to find flattened eggs.

Example
-------

[zip]
recipe = zipeggs:zipeggs
target = dist
source = eggs
