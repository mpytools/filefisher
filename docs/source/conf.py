# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Import packages ---------------------------------------------------------

import datetime
import os
import subprocess
import sys
from importlib.metadata import version

import filefisher

# -- Display version info ----------------------------------------------------
# for debugging on RTD

on_rtd = os.environ.get("READTHEDOCS", None) == "True"
if on_rtd:

    print("python exec:", sys.executable)
    print("sys.path:", sys.path)
    print("os.getcwd():", os.getcwd())

    if "CONDA_DEFAULT_ENV" in os.environ or "conda" in sys.executable:
        print("conda environment:")
        subprocess.run([os.environ.get("CONDA_EXE", "conda"), "list"])
    else:
        print("pip environment:")
        subprocess.run([sys.executable, "-m", "pip", "list"])

    print(f"filefisher: {filefisher.__version__=}, {filefisher.__file__=}")


# -- Project information -----------------------------------------------------

project = "filefisher"
copyright_year = datetime.date.today().year
copyright = (
    f"(c) 2024-{copyright_year} Mathias Hauser"
)

authors = "Mathias Hauser"
author = authors

# The full version, including alpha/beta/rc tags
release = version("filefisher")
# The short X.Y version
version = ".".join(release.split(".")[:2])


# -- General configuration ---------------------------------------------------

# add sphinx extension modules
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "IPython.sphinxext.ipython_directive",
    "IPython.sphinxext.ipython_console_highlighting",
]

autosummary_generate = True

napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_param = False
napoleon_use_rtype = False

# napoleon_use_ivar = True
# napoleon_use_admonition_for_notes = True

numpydoc_class_members_toctree = True
numpydoc_show_class_members = False

autodoc_typehints = "none"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = "sphinx_book_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = []

pygments_style = "sphinx"
