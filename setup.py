# Copyright (C) 2015 Red Hat
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Adam Williamson <awilliam@redhat.com>

import os
from setuptools import setup, find_packages

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    LONGDESC = f.read()

setup(
    name = "openqa_client",
    version = "2.0.1",
    author = "Adam Williamson",
    author_email = "awilliam@redhat.com",
    description = "openQA client",
    license = "GPLv2+",
    keywords = "openqa opensuse fedora client",
    url = "https://github.com/os-autoinst/openQA-python-client",
    packages = ["openqa_client"],
    install_requires = ['requests', 'setuptools', 'six'],
    long_description=LONGDESC,
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v2 or later "
        "(GPLv2+)",
    ],
)
