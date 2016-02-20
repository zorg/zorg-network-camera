#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

try:
    from pypandoc import convert
    readme = lambda f: convert(f, "rst")
except ImportError:
    print("Module pypandoc not found, could not convert Markdown to RST")
    readme = lambda f: open(f, "r").read()

req = open("requirements.txt")
requirements = req.readlines()

version_string = __import__('zorg_network_camera').__version__

setup(
    name="zorg-network-camera",
    version=version_string,
    url="https://github.com/zorg/zorg-network-camera",
    description="A module which includes various network camera utilities.",
    long_description=readme("README.md"),
    author="Zorg Group",
    author_email="gunthercx@gmail.com",
    packages=find_packages(),
    package_dir={"zorg_network_camera": "zorg_network_camera"},
    install_requires=requirements,
    license="MIT",
    zip_safe=True,
    platforms=["any"],
    keywords=["zorg", "network", "ip", "camera"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    test_suite="tests",
    tests_require=[]
)
