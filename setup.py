# coding: utf-8

"""
    GroupDocs.Translation SDK

    The version of the OpenAPI document: 24.12.0
    Contact: anton.perhunov@aspose.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""
from pathlib import Path
from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "groupdocs-translation-cloud"
VERSION = "25.6.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]
this_directory = Path(__file__).parent #path.abspath(path.dirname(__file__))
with open(Path(this_directory, 'README.md').resolve(), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name=NAME,
    version=VERSION,
    description="GroupDocs.Translation SDK",
    author="GroupDocs",
    author_email="anton.perhunov@aspose.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "GroupDocs.Translation SDK"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description_content_type='text/markdown',
    long_description=long_description,
    package_data={"groupdocs_translation_cloud": ["py.typed"]},
)
