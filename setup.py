from setuptools import setup, find_packages

setup(
    name="buff163_price_getter",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        "requests",
        "currency_convert",
        "aiohttp"
    ],
)