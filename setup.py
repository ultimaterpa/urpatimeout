import pathlib
from setuptools import setup

here = pathlib.Path(__file__).parent
readme = (here / "README.md").read_text()

about = {}
with open(here / "urpatimeout" / "__about__.py") as f:
    exec(f.read(), about)

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    url=about["__url__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    license=about["__license__"],
    keywords="Robotic Process Automation, RPA, UltimateRPA, timeout, time limit",
    packages_data={"urpatimeout": ["py.typed"]},
    packages=["urpatimeout"],
    python_requires=">=3.7",
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    zip_safe=False,
    include_package_data=True,
)
