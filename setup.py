import setuptools
from distutils.util import convert_path

with open("README.md", "r") as fh:
    long_description = fh.read()

metadata = {}
ver_path = convert_path('opencitingpy/metadata.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), metadata)


setuptools.setup(
    name="opencitingpy",
    version=metadata['__version__'],
    author=metadata['__author__'],
    author_email=metadata['__email__'],
    description="Python tool for easily making requests to the OpenCitations API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/unaisaralegui/opencitingpy",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
