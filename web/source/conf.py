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
    128,
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

# -- Options for internationalization ----------------------------------------

language = "ja"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# setting of opengraph
# https://pypi.org/project/sphinxext-opengraph/
extensions += ["sphinxext.opengraph"]
ogp_site_url = f"https://kicon.musicscience37.com/{language}/"
ogp_site_name = "KIcon"
ogp_image = "https://kicon.musicscience37.com/KIcon128white.png"

html_theme = "sphinx_orange_book_theme"
html_static_path = ["_static"]
html_css_files = ["kicon.css"]

html_title = "KIcon"

html_logo = "https://kicon.musicscience37.com/KIcon80.png"
html_favicon = "https://kicon.musicscience37.com/KIcon.ico"

html_theme_options = {
    "show_prev_next": False,
    "logo": {
        "text": html_title,
    },
    "pygment_light_style": "gruvbox-light",
    "pygment_dark_style": "native",
    "repository_url": "https://gitlab.com/MusicScience37/kicon",
    "use_repository_button": True,
}
