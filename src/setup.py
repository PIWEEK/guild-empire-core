from distutils.core import setup

setup(
    name='guild-empire-core',
    version='0.1.0',
    description='Guild empire core',
    author='Guild empire core team',
    author_email='guild-empire@googlegroups.com',
    url='piweek',
    packages=['actions', 'characters', 'games', 'guilds', 'places', 'storage'],
    py_modules=['exceptions', 'utils']
)
