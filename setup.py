import setuptools

VERSION = "2.1.5"

with open("README.md", "r") as file_object:
    LONG_DESCRIPTION = file_object.read()

setuptools.setup(
    name="repulsiveruby",
    version=VERSION,
    author="Quan Wang",
    author_email="quanrpi@gmail.com",
    description="RepulsiveRuby: A game made with Pygame",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/wq2012/RepulsiveRuby",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
