from setuptools import setup, find_packages

setup(
  name='pyclique',
  version='0.1.0',
  description='Setting up a python package',
  author='Rogier van der Geer',
  author_email='rogiervandergeer@godatadriven.com',
  url='https://github.com/peekxc/pyclique',
  packages=find_packages(include=['src/pyclique'])
)