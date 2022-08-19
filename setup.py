from setuptools import setup

## Raw setuptools
## Note: don't remove package_dir, and don't use find_packages
# setup(
#   name = 'pyclique',  
#   package_dir = {'': 'src'}, 
#   packages = ['pyclique']
# )

## Mypyc setup 
from mypyc.build import mypycify
setup(
  name = 'pyclique',  
  package_dir = {'': 'src'}, 
  packages = ['pyclique'],
  ext_modules = mypycify([
    '--disallow-untyped-defs',
    'src/pyclique/set_util_typed.py'
  ])
)

## Cython setup 
# from Cython.Build import cythonize
# setup(
#   ext_modules = cythonize("src/pyclique/set_util_native.pyx", language_level="3", annotate=False)
#   # name='pyclique',
#   # packages=['src/pyclique'],
#   # ext_modules=mypycify([
#   #   # 'src/pyclique/__init__.py',
#   #   'src/pyclique/set_util_fast.py',
#   # ]),
# )