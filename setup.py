# coding=utf-8

from setuptools import setup, find_packages

setup(
    name="math_service",
    version='1.0',
    description="Math related API Service",
    author="hao.yuan",
    author_email="yuanhao12@gmail.com",
    packages=['v1'],
    install_requires=['Flask', 'Flask-RESTful'],
)
