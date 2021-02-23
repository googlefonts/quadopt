# coding: utf-8
# Copyright 2013 The Font Bakery Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# See AUTHORS.txt for the list of Authors and LICENSE.txt for the License.

import os
from setuptools import find_packages, setup, Extension
from Cython.Build import cythonize


extensions = [
    Extension(
        "fontcrunch._quadopt",
        sources=["src/fontcrunch/_quadopt.pyx", "src/fontcrunch/quadopt.cc"],
        extra_compile_args=["-std=c++11", "-O3"] if os.name == "posix" else [],
        language="c++",
    ),
]

setup(
    name="FontCrunch",
    use_scm_version={"write_to": "src/fontcrunch/_version.py"},
    url="https://github.com/googlefonts/fontcrunch/",
    description="fontcrunch",
    author="Raph Levien",
    package_dir={"": "src"},
    packages=find_packages("src"),
    zip_safe=False,
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    setup_requires=["cython", "setuptools_scm"],
    install_requires=["fonttools"],
    extras_require={
        "plot": ["reportlab"],
    },
    ext_modules=cythonize(extensions),
    entry_points={
        "console_scripts": [
            "font-crunch = fontcrunch.cli:main",
        ]
    },
)
