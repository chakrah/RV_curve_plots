import setuptools

setuptools.setup(
name= "rv_curve_jura",
version="0.1",
author="Hritam Chakraborty",
author_email="Hritam.Chakraborty@unige.ch",
description="Plot all RV curves you want!",
packages= setuptools.find_packages(),
install_requires=["numpy", "matplotlib"],
classifiers=["Programming Language :: Python :: 3"],
)
