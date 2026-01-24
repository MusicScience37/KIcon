"""Configuration file for Sphinx."""

project = "KIcon"
copyright = "2026, MusicScience37 (Kenta Kabashima)"
author = "MusicScience37 (Kenta Kabashima)"

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = []
exclude_patterns = []

language = "en"


# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_orange_book_theme"
html_static_path = ["_static"]
html_css_files = [
    "custom.css",
]

html_favicon = "../../outputs/KIcon.ico"

html_theme_options = {
    "show_prev_next": False,
    "logo": {
        "image_light": "../../outputs/KIcon.svg",
        "image_dark": "../../outputs/KIcon-dark.svg",
        "text": project,
    },
    "pygments_light_style": "gruvbox-light",
    "pygments_dark_style": "native",
    "repository_url": "https://gitlab.com/MusicScience37/kicon",
    "use_repository_button": True,
    "use_source_button": True,
    "path_to_docs": "web/source",
}
