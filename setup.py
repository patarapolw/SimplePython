from setuptools import setup, find_packages

setup(
    name='MyUtils',
    version='0.1.0',
    packages=find_packages(exclude=['tests']),
    tests_require=['pytest']
)
