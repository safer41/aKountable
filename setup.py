import os

from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
install_requires = [
    "keras==2.0.0",
    "tensorflow==2.5.0"
]

setup(
    name='aKountable',
    version='2.0.0',
    description='aKountable: Safe, accountable AI in the Blockchain',
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: The people/Big companies",
        "License :: OSI Approved :: Apache 2.0",
        "Programming Language :: Python :: 2.7",
    ],
    url='https://github.com/safer41/aKountable.git',
    author='41',
    keywords='AI, blockchain, safety, saferAI',
    license="Apache 2.0",
    packages=find_packages(),
    include_package_data=False,
    zip_safe=False,
    install_requires=install_requires
)
