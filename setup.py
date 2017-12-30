from setuptools import setup

setup(
  name='asana-alfred',
  version='1.0',
  description='Asana-Alfred integration',
  author='Alexander Luberg',
  author_email='alex@luberg.me',
  install_requires=[
    'asana==0.6.5',
    'alfred-workflow==1.32',
  ],
)
