def load_version(path: str) -> str:
    with open(path, 'r') as f:
        return f.readline().strip()


NAME: str = 'somni-log'
DESCRIPTION: str = 'A minimal Logger-setup for Python'
LONG_DESCRIPTION: str = None
VERSION: str = load_version('VERSION')

AUTHOR: str = 'Samu Rabin'
AUTHOR_EMAIL: str = 'samus_codes@samusoft.net'
MAINTAINER: str = 'Samu Rabin'
MAINTAINER_EMAIL: str = 'samus_codes@samusoft.net'

LONG_DESCRIPTION_CONTENT_TYPE: str = 'text/markdown'
INSTALL_REQUIRES: list[str] = []
KEYWORDS: list[str] = ['logging', 'logger', 'minimal']
CLASSIFIERS: list[str] = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3.11',
    'Topic :: Software Development :: Libraries :: Python Modules'
]
