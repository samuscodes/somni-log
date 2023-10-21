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


class License:
    KEY: str
    LICENSE_TEXT: str


class MIT(License):
    KEY: 'MIT'
    LICENSE_TEXT: str = ('MIT License\n'
                         '\n'
                         'Copyright (c) [<YEAR>] [<FULLNAME>]\n'
                         '\n'
                         'Permission is hereby granted, free of charge, to any person obtaining a copy\n'
                         'of this software and associated documentation files (the "Software"), to deal\n'
                         'in the Software without restriction, including without limitation the rights\n'
                         'to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n'
                         'copies of the Software, and to permit persons to whom the Software is\n'
                         'furnished to do so, subject to the following conditions:\n'
                         '\n'
                         'The above copyright notice and this permission notice shall be included in all\n'
                         'copies or substantial portions of the Software.\n'
                         '\n'
                         'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n'
                         'IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n'
                         'FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n'
                         'AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n'
                         'LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n'
                         'OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n'
                         'SOFTWARE.')
