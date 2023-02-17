from setuptools import setup

setup(
    name='openapiToDocx',
    version='0.1',
    packages=['openapiToDocx'],
    install_requires=[
        'PyYAML==5.4.1',
        'python-docx==0.8.11',
    ],
)