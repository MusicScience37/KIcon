#!/usr/bin/env python3
"""Tool for this repository."""

import pathlib
import subprocess
import typing

import click

THIS_DIR = pathlib.Path(__file__).absolute().parent


@click.group()
def cli():
    pass


# #############################################################################
# Conversion of images
# #############################################################################

IMAGE_DENSITY = 1024


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


OUTPUTS_DIR = THIS_DIR / "outputs"


def _execute_command(command: typing.List[str]):
    click.echo(click.style(f"$ {' '.join(command)}", bold=True))
    subprocess.run(command, cwd=OUTPUTS_DIR, check=True)


def _convert_one_image(size: int, transparent: bool, suffix: str):
    output_filename = f"KIcon{size}"
    if not transparent and suffix == "png":
        output_filename = output_filename + "white"
    output_filename = output_filename + "." + suffix

    command = [
        "convert",
        "-density",
        str(IMAGE_DENSITY),
        str("KIcon.png"),
        "-resize",
        f"{size}x{size}",
    ]
    if not transparent:
        command = command + ["-alpha", "remove", "-alpha", "off"]
    command = command + [str(output_filename)]

    _execute_command(command)


def _convert_png():
    suffix = "png"
    for transparent in [True, False]:
        for size in IMAGE_SIZES:
            _convert_one_image(
                size=size,
                transparent=transparent,
                suffix=suffix,
            )


def _convert_jpg():
    suffix = "jpg"
    transparent = False
    for size in IMAGE_SIZES:
        _convert_one_image(
            size=size,
            transparent=transparent,
            suffix=suffix,
        )


def _convert_icon():
    command = ["convert"]
    for size in ICON_SIZES:
        command = command + [f"KIcon{size}.png"]
    command = command + ["KIcon.ico"]

    _execute_command(command)


@cli.command()
def convert():
    """Convert SVG to other image types."""
    _convert_png()
    _convert_jpg()
    _convert_icon()


# #############################################################################
# Web
# #############################################################################


WEB_DIR = THIS_DIR / "web"

SUPPORTED_LANGUAGES = ["ja", "en"]


@cli.command()
def update():
    """Update translation files."""

    subprocess.run(
        [
            "sphinx-build",
            "-M",
            "gettext",
            "source",
            "build",
        ],
        check=True,
        cwd=str(WEB_DIR),
    )
    subprocess.run(
        [
            "sphinx-intl",
            "update",
            "-p",
            "../build/gettext",
            "-l",
            "en",
        ],
        check=True,
        cwd=str(WEB_DIR / "source"),
    )


@cli.command()
@click.option("-p", "--port", default=2496, help="Port of the HTTP server.", type=int)
def auto(port: int):
    """Automatic build and view."""

    subprocess.run(
        [
            "sphinx-autobuild",
            "source",
            "build/auto_build",
            "--host",
            "0",
            "--port",
            str(port),
        ],
        check=False,
        cwd=str(WEB_DIR),
    )


@cli.command()
@click.option(
    "-l",
    "--language",
    default="ja",
    help="Language.",
    type=click.Choice(SUPPORTED_LANGUAGES, case_sensitive=True),
)
def build(language: str):
    """Build document."""

    subprocess.run(
        [
            "sphinx-build",
            "-M",
            "html",
            "source",
            f"build/{language}",
            "-D",
            f"language={language}",
            "-D",
            f"ogp_site_url=https://kicon.musicscience37.com/{language}/",
        ],
        check=True,
        cwd=str(WEB_DIR),
    )


DEFAULT_PORTS = {
    "ja": 2497,
    "en": 2498,
}


@cli.command()
@click.option(
    "-l",
    "--language",
    default="ja",
    help="Language.",
    type=click.Choice(SUPPORTED_LANGUAGES, case_sensitive=True),
)
@click.option("-p", "--port", default=None, help="Port of the HTTP server.", type=int)
def view(language: str, port: typing.Optional[int]):
    """View HTML files."""

    if port is None:
        port = DEFAULT_PORTS[language]

    subprocess.run(
        ["python3", "-m", "http.server", str(port)],
        check=False,
        cwd=str(WEB_DIR / "build" / str(language) / "html"),
    )


if __name__ == "__main__":
    cli()
