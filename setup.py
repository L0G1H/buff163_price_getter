from setuptools import setup, find_packages

setup(
    name='buff_price_getter',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'currency_convert'
    ],
)