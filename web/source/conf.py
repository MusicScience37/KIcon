# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


ICON_SIZES = [
    16,
    32,
    48,
    64,
    192,
]

IMAGE_SIZES = ICON_SIZES + [
    24,
    80,
    152,
    180,
    512,
    1024,
]
IMAGE_SIZES.sort()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "KIcon"
copyright = "2022, MusicScience37 (Kenta Kabashima)"
author = "MusicScience37"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = []
exclude_patterns = []

# setting of sphinx-jinja
extensions += ["sphinx_jinja"]
jinja_contexts = {
    "image_context": {
        "image_sizes": IMAGE_SIZES,
    }
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# setting of opengraph
# https://pypi.org/project/sphinxext-opengraph/
extensions += ["sphinxext.opengraph"]
ogp_site_url = "https://kicon.musicscience37.com/en/"
ogp_site_name = "KIcon"
ogp_image = "https://kicon.musicscience37.com/KIcon128white.png"

html_theme = "sphinx_rtd_theme"
html_static_path = []

html_title = "MusicScience37"

html_logo = "https://kicon.musicscience37.com/KIcon80white.png"
html_favicon = "https://kicon.musicscience37.com/KIcon.ico"

html_theme_options = {
    "navigation_depth": -1,
    "style_nav_header_background": "#B24700",
}

# -- Options for internationalization ----------------------------------------

language = "ja"
