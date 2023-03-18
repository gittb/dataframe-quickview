from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dataframe-quickview",
    version="0.1.0",
    author="Ben Gitter",
    author_email="gittebd@gmail.com",
    description="A simple package to extend pandas DataFrame functionality for web-based visualization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gittb/dataframe-quickview",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask>=2.0.1",
        "pandas>=1.3.0",
        "Flask-Testing>=0.8.0"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires='>=3.6',
)