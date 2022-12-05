from distutils.core import setup
from setuptools import find_packages

setup(name='snowflake',
      version='0.1',
      author='Abhinav Choudhary',
      author_email='abhinavchoudhary100@gmail.com',
      packages=find_packages(),
      install_requires=["numpy","turtle","random"]
     )