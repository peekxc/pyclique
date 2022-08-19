from setuptools import setup

## Mypyc setup 
from mypyc.build import mypycify
setup(
  name = 'pyclique',  
  packages = ['src/pyclique'],
  ext_modules = mypycify([
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