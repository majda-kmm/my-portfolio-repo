from setuptools import setup, find_packages

setup(
    name='question2',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scikit-learn',
        'matplotlib',
        'plotly'
    ],
    author='Majda',
    description='Mini package de modelisation',
)