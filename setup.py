from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in site_planning/__init__.py
from site_planning import __version__ as version

setup(
	name="site_planning",
	version=version,
	description="site_planning",
	author="indictrans",
	author_email="aakash.k@indictranstech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
