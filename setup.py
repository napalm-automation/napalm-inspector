"""setup.py file."""
from setuptools import find_packages, setup

with open("requirements.txt", "r") as fs:
    reqs = [r for r in fs.read().splitlines() if (len(r) > 0 and not r.startswith("#"))]

with open("README.md", "r") as fs:
    long_description = fs.read()

setup(
    name="napalm-inspector",
    version="1.0.0",
    packages=find_packages(exclude=("test*",)),
    test_suite="test_base",
    author="Patrick Ogenstad",
    author_email="patrick@ogenstad.com",
    description="Web application to test NAPALM getters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Topic :: Utilities",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    url="https://github.com/napalm-automation/napalm-inspector",
    include_package_data=True,
    install_requires=reqs,
)
