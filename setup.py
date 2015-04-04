from setuptools import setup

setup(
    name='cms50e',
    description='Read pulse oximetry data from CMS50E device',
    install_requires=[
        'pyserial',
        'blessings'
    ]
)
