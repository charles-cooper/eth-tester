#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    find_packages,
    setup,
)

extras_require = {
    "dev": [
        "build>=0.9.0",
        "bumpversion>=0.5.3",
        "ipython",
        "pre-commit>=3.4.0",
        "tox>=4.0.0",
        "twine",
        "wheel",
    ],
    "docs": [
        "towncrier>=21,<22",
    ],
    "test": [
        "pytest>=7.0.0",
        "pytest-xdist>=2.0.0,<3",
        "eth-hash[pycryptodome]>=0.1.4,<1.0.0",
    ],
    "py-evm": [
        # Pin py-evm to exact version, until it leaves alpha.
        # EVM is very high velocity and might change API at each alpha.
        "py-evm==0.9.0b1",
        "eth-hash[pysha3]>=0.1.4,<1.0.0;implementation_name=='cpython'",
        "eth-hash[pycryptodome]>=0.1.4,<1.0.0;implementation_name=='pypy'",
    ],
}

extras_require["dev"] = (
    extras_require["dev"]
    + extras_require["docs"]
    + extras_require["test"]
    + extras_require["py-evm"]
)
# convenience in case someone leaves out the `-`
extras_require["pyevm"] = extras_require["py-evm"]

with open("./README.md") as readme:
    long_description = readme.read()

setup(
    name="eth-tester",
    # *IMPORTANT*: Don't manually change the version here. Use the 'bumpversion' utility.
    version="0.10.0-beta.3",
    description="""eth-tester: Tools for testing Ethereum applications.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="The Ethereum Foundation",
    author_email="snakecharmers@ethereum.org",
    url="https://github.com/ethereum/eth-tester",
    include_package_data=True,
    install_requires=[
        "eth-abi>=3.0.1",
        "eth-account>=0.6.0",
        "eth-keys>=0.4.0",
        "eth-utils>=2.0.0",
        "rlp>=3.0.0",
        "semantic_version>=2.6.0",
    ],
    extras_require=extras_require,
    python_requires=">=3.8,<4",
    py_modules=["eth_tester"],
    license="MIT",
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"eth_tester": ["py.typed"]},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
