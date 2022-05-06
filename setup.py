from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ezzdl",
    version="1.0.0",
    scripts=["download.py"],
    author="BarsTiger",
    description="Cool download manager based on rich and its sample code",
    long_description=long_description,
    py_modules=["ezzdl"],
    license='MIT',
    url='https://github.com/BarsTiger/ezzdl',
    long_description_content_type="text/markdown",
    keywords=["threading", "thread", "decorator", "crossplatform"],
    install_requires=["rich"]
)
