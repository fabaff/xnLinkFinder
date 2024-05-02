#!/usr/bin/env python
import os
import shutil
from setuptools import setup, find_packages

setup(
    name="xnLinkFinder",
    packages=find_packages(),
    version=__import__('xnLinkFinder').__version__,
    description="A python script to find endpoints from a URL, a file of URLs, a directory of files, a Burp XML file or a ZAP ASCII message file. It also gets potential parameters and a target specific wordlist.",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    author="@xnl-h4ck3r",
    url="https://github.com/xnl-h4ck3r/xnlLinkFinder",
    py_modules=["xnLinkFinder"],
    install_requires=[
      "requests",
      "psutil",
      "pyyaml",
      "termcolor",
      "beautifulsoup4",
      "lxml",
      "html5lib",
      "urllib3"
    ],
    entry_points={
        'console_scripts': [
            'xnLinkFinder = xnLinkFinder.xnLinkFinder:main',
        ],
    },
)
