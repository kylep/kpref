"""Set up kpref-py-api """
from setuptools import setup, find_packages

setup(
    name="kpref-py-api",
    packages=find_packages(),
    version="1.0",
    license="",
    description="Python API for reference project",
    author="Kyle Pericak",
    author_email="kyle@pericak.com",
    python_requires=">=3.0.0",
    zip_safe=False,
    install_requires=["uvicorn", "Quart"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
    ],
)
