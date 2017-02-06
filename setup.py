from setuptools import setup, find_packages
setup(
    name = "pixypy",
    version = "0.0.1",
    packages = find_packages(),
    # installed or upgraded on the target machine
    install_requires = ['flask>=0.12'],
    # metadata for upload to PyPI
    author = "salesiopark",
    author_email = "salesiopark@gmail.com",
    description = "python wrapper for PixiJS v4",
    license = "PSF",
    keywords = "pixi PixiJS python wrapper",
    url = "http://pixipy.blogspot.com",   # project home page, if any
    # could also include long_description, download_url, classifiers, etc.
    classifiers = ['Programming Language :: Python :: 3.4'],
)