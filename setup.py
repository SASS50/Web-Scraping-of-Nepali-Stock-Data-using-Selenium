from setuptools import setup, find_packages

setup(
    name='scrap_library',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'pandas',
    ],
)
