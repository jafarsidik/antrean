from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in antrean/__init__.py
from antrean import __version__ as version

setup(
	name="antrean",
	version=version,
	description="Aplikasi Antrean Sistem Informasi Rumah Sakit, Brdiging dengan BPJS",
	author="Muhamad Jafar Sidik",
	author_email="jeff.sidik@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
