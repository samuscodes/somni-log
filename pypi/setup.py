from setuptools import setup, find_packages
from constants import *
import os


setup(
    name=NAME,
    description=DESCRIPTION,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS
)
