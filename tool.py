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


def _convert_one_image(size: int, transparent: bool, is_dark: bool, suffix: str):
    icon_type = ""
    if is_dark:
        icon_type = "-dark"

    output_filename = f"KIcon{size}{icon_type}"
    if not transparent and suffix == "png":
        output_filename = output_filename + "white"
    output_filename = output_filename + "." + suffix

    command = [
        "convert",
        "-density",
        str(IMAGE_DENSITY),
        str(f"KIcon{icon_type}.png"),
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
        for is_dark in [True, False]:
            if not transparent and is_dark:
                # 白背景のダークテーマのアイコンは見た目が良くないためスキップ
                continue
            for size in IMAGE_SIZES:
                _convert_one_image(
                    size=size,
                    transparent=transparent,
                    is_dark=is_dark,
                    suffix=suffix,
                )


def _convert_jpg():
    suffix = "jpg"
    transparent = False
    for size in IMAGE_SIZES:
        _convert_one_image(
            size=size,
            transparent=transparent,
            is_dark=False,
            suffix=suffix,
        )


def _convert_icon():
    for icon_type in ["", "-dark"]:
        command = ["convert"]
        for size in ICON_SIZES:
            command = command + [f"KIcon{size}{icon_type}.png"]
        command = command + [f"KIcon{icon_type}.ico"]

        _execute_command(command)


@cli.command()
def convert():
    """Convert SVG to other image types."""
    _convert_png()
    _convert_jpg()
    _convert_icon()


if __name__ == "__main__":
    cli()
