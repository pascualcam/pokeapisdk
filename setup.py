from setuptools import setup, find_packages

setup(
    name="pokeapisdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "click",
        "dataclasses",
        "unittest",
    ],
    description="A simple collection of classes to interact with the PokeAPI",
    author="Pascual Camacho",
    author_email="me@pascualcam.com",
    url="https://github.com/pascualcam/pokeapisdk/",
)
