from distutils.core import setup

setup(
  name = 'guild-empire-core',
  version = '0.1.0',
  description = 'Guild empire core',
  author = 'Guild empire core team',
  author_email = 'guild-empire@googlegroups.com',
  url = 'piweek',
  packages = ['src/actions', 'src/characters', 'src/games',
              'src/guilds', 'src/places', 'src/storage',
              'definitions'],
  include_package_data=True,
  py_modules = ['src/exceptions', 'src/utils',]
)
