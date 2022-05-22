from setuptools import setup

setup(
   name='IA_Aestrella',
   version='1.0',
   description='Something different',
   author='Augusto Noguera',
   author_email='augusto_nog@outlook.es',
   packages=['IA_Aestrella'],  # would be the same as name
   include_package_data=True,
   install_requires=['autopep8', 'cycler', 'fonttools', 'kiwisolver', 'matplotlib', 'numpy', 'packaging', 'graphviz', 'pygraphviz'], #external packages acting as dependencies
   entry_points={"console_scripts": ["realpython=reader.__main__:main"]}
)