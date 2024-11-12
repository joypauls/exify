import click
from PIL import Image, ExifTags
from rich.console import Console
from rich.table import Table
from rich import box

from exify import __version__
from exify.utils import decimal_to_fraction, get_file_name_from_path

# from typing import List, Tuple

# from PIL.ExifTags import TAGS

HELP_TEXT = f"Exify {__version__}"


######################
# Root-Level Command #
######################


@click.group(help=HELP_TEXT)
@click.version_option()
def cli():
    """Container object for the app"""
    # click.echo("<CLI Root> beep boop")


# @click.group(invoke_without_command=True, help=HELP_TEXT)
# @click.argument("file", type=click.Path(exists=True))
# @click.pass_context
# def cli(ctx, file):
#     """Container object for the app"""
#     if ctx.invoked_subcommand is None:
#         # root-level command behavior
#         click.echo(f"Reading file {file}")
#     else:
#         # if a subcommand is called, this block is skipped
#         pass


# @cli.command()
# @click.option(
#     "-f",
#     default=None,
#     help="",
# )
# def play(f):
#     """Play a video file"""
#     click.echo(f"File {f}!")
#     p = Player(file=f)
#     p.play()


# @cli.command()
# @click.option(
#     "-d",
#     default=None,
#     help="Directory with files to process - can also be a single video file.",
# )
# def process(d):
#     """Main processing pipeline"""
#     click.echo(f"Directory {d}!")


########################
# Primary Client Usage #
########################


DEFAULT_TAG_NAMES = [
    "DateTimeOriginal",
    "Make",
    "Model",
    "LensModel",
    "FocalLength",
    "ExposureTime",
    "FNumber",
    "ISOSpeedRatings",
]
DEFAULT_TAG_NAMES_MAP = {
    "DateTimeOriginal": "Date & Time",
    "Make": "Camera Make",
    "Model": "Camera Model",
    "LensModel": "Lens",
    "FocalLength": "Focal Length",
    "ExposureTime": "Shutter Speed",
    "FNumber": "F-Stop",
    "ISOSpeedRatings": "ISO",
}


# def print_exif(exif_list: List[Tuple[str, str]]):
#     console = Console()
#     table = Table(title="EXIF Data")
#     table.add_column("Tag")
#     table.add_column("Value")
#     for tag, value in exif_list:
#         table.add_row(tag, value)
#     console.print(table)


@cli.command(help="View the metadata of an image file.")
# @click.option(
#     "-f",
#     default=None,
#     help="",
# )
@click.argument("file", type=click.Path(exists=True))
def view(file):
    # click.echo(f"Reading file: {file}")
    image = Image.open(file)
    exif_data = image._getexif()
    # exif_data = extract_exif_data(image)
    if exif_data:
        processed_exif_data = {}
        # first loop to process
        for tag, value in exif_data.items():
            if len(str(value)) > 50:
                value = "<hidden>"
            tag_name = ExifTags.TAGS.get(tag, tag)
            if tag_name in DEFAULT_TAG_NAMES:
                processed_exif_data[tag_name] = value
                # special handling for ExposureTime
                if tag_name == "ExposureTime":
                    processed_exif_data[tag_name] = decimal_to_fraction(value)

        # all_exif = get_ifd_tags(exif_data)

        # sorts the keys in the order of DEFAULT_TAG_NAMES
        sorted_key_value_list = [
            (key, processed_exif_data[key])
            for key in DEFAULT_TAG_NAMES
            if key in processed_exif_data
        ]

        # second loop to print
        console = Console()
        table = Table(
            title=f"[bold purple]Exif Data[/] ({get_file_name_from_path(file)})",
            box=box.HORIZONTALS,
        )
        table.add_column("Tag")
        table.add_column("Value")
        for key, value in sorted_key_value_list:
            readable_key = DEFAULT_TAG_NAMES_MAP.get(key, key)
            # print(readable_key.__class__)
            # print(value.__class__)
            table.add_row(readable_key, str(value))
            # print(f"{readable_key}: {value}")
        console.print(table)
    else:
        print("No EXIF data found.")


# @cli.command(help="Edit the metadata of a file.")
# # @click.option(
# #     "-f",
# #     default=None,
# #     help="",
# # )
# @click.argument("file", type=click.Path(exists=True))
# def edit(file):
#     click.echo(f"Reading file: {file}")


########################
# Development Commands #
########################


# @cli.command(help="Puppet command for testing.")
# # @click.option(
# #     "-f",
# #     default=None,
# #     help="",
# # )
# @click.argument("file", type=click.Path(exists=True))
# def puppet(file):
#     click.echo(f"Reading file: {file}")
