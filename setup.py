import pathlib
from setuptools import setup
import miaowware_sphinx_theme.__info__ as info

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name=info.__project__,
    version=info.__version__,
    description=info.__summary__,
    long_description=README,
    long_description_content_type="text/markdown",
    url=info.__webpage__,
    author=info.__author__,
    author_email=info.__email__,
    license=info.__license__,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: Internet",
        "Topic :: Software Development :: Documentation",
        "Framework :: Sphinx :: Theme"
    ],
    packages=["miaowware_sphinx_theme"],
    package_data={
        "miaowware_sphinx_theme": ["py.typed"]
    },
    install_requires=["sphinx>=1.6.0"],
    entry_points={
        "sphinx.html_themes": [
            "miaowware = miaowware_sphinx_theme",
        ]
    },
)
