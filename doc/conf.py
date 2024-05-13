# Configuration file for the Sphinx documentation builder
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# Project information
project = "gletter"
copyright = "2024, zhengxyz123"
author = "zhengxyz123"
release = "0.0.1"

# General configuration
extensions = [
    "notfound.extension",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx_autodoc_typehints",
]
autosummary_generate = False
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "pyglet": ("https://pyglet.readthedocs.io/en/latest", None),
}

# Autodoc settings
autodoc_default_options = {
    "member-order": "bysource",
    "exclude-members": "__new__",
}
autodoc_class_signature = "separated"

# sphinx_autodoc_typehints configuration
typehints_use_signature = True
typehints_use_signature_return = True
always_use_bars_union = True

# Napoleon settings
napoleon_numpy_docstring = False
napoleon_include_special_with_doc = True

# Options for HTML output
html_theme = "furo"
html_static_path = ["_static"]
