import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
name= "rv_curve_jura",
version="0.1",
author="Hritam Chakraborty",
author_email="Hritam.Chakraborty@unige.ch",
description="Plot all RV curves you want!",
packages=setuptools.find_packages(),
long_description=long_description,
long_description_content_type="text/markdown",
url="https://github.com/hritamchakraborty/RV_curve_plots",
install_requires=["numpy", "matplotlib"],
classifiers=["Programming Language :: Python :: 3"],
)
