from setuptools import setup, find_packages

setup(
    name="python",
    version="0.0.1",
    packages=find_packages(),
#    package_data={"": "lib/libsfencrypt.so"},
    include_package_data=True
)
