from setuptools import setup, find_packages

setup(
    name="us_visa",
    version="0.0.1",
    author="Stephen",
    author_email="acheampongstephen392024@gmail.com",
    description="A production-ready MLOps project for US visa prediction",
    packages=find_packages(include=["us_visa", "us_visa.*"]),
    install_requires=[],  # Leave it empty if you're using requirements.txt
)
