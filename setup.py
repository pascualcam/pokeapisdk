from setuptools import setup, find_packages

setup(
    name="pokeapisdk",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "click",
        "dataclasses",
    ],
    description="A simple collection of classes to interact with the PokeAPI",
    author="Pascual Camacho",
    author_email="me@pascualcam.com",
    url="https://github.com/pascualcam/pokeapisdk/",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)
