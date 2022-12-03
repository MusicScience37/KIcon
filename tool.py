#!/usr/bin/env python3
"""Tool for this repository."""

import pathlib
import subprocess
import typing

import click


@click.group()
def cli():
    pass


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
    152,
    180,
    512,
    1024,
]
IMAGE_SIZES.sort()


THIS_DIR = pathlib.Path(__file__).absolute().parent
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
        str("KIcon.svg"),
        "-resize",
        f"{size}x{size}",
    ]
    if transparent:
        command = command + ["-transparent", "white"]
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
    command = command + ["-colors", "256", "KIcon.ico"]

    _execute_command(command)


@cli.command()
def convert():
    """Convert SVG to other image types."""
    _convert_png()
    _convert_jpg()
    _convert_icon()


if __name__ == "__main__":
    cli()
