#!/usr/bin/env python

# Copyright (c) Facebook, Inc. and its affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from setuptools import setup, find_packages

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name="vilbert_multi_task",
    version="0.1.0",
    author="Jiasen Lu, Vedanuj Goswami",
    description="",
    license="MIT",
    zip_safe=True,
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    dependency_links=['https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.5.0-py3-none-any.whl']

)
