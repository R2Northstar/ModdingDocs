# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "Northstar Modding"
copyright = "2022, Northstar Developer Team"
author = "Northstar Developer Team"

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_design",
    "sphinxcontrib.youtube",
    "sphinx_copybutton",
    "sphinx_rsquirrel",
    "sphinxext.opengraph",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

exclude_patterns = ["_build"]

# -- Options for HTML output

html_theme = "furo"

html_static_path = ["_static"]
ogp_site_url = "https://r2northstar.readthedocs.io/"
ogp_image = "https://northstar.tf/assets/logo_1k.png"

# -- Options for EPUB output
epub_show_urls = "footnote"

highlight_language = "squirrel"

# furo theme specific
pygments_dark_style = "one-dark"
