"""This is largely a dev utility for now, but it will be the primary entry point for the app."""

import click

HELP_TEXT = "EXIFy v0.1.0"


##########################
# Primary User Interface #
##########################


@click.group(help=HELP_TEXT)
@click.version_option()
def cli():
    """Container object for the app"""
    click.echo("<CLI Root> beep boop")


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


@cli.command(help="View the metadata of a file.")
# @click.option(
#     "-f",
#     default=None,
#     help="",
# )
@click.argument("file", type=click.Path(exists=True))
def view(file):
    click.echo(f"Reading file: {file}")


@cli.command(help="Edit the metadata of a file.")
# @click.option(
#     "-f",
#     default=None,
#     help="",
# )
@click.argument("file", type=click.Path(exists=True))
def edit(file):
    click.echo(f"Reading file: {file}")


########################
# Development Commands #
########################


@cli.command(help="Puppet command for testing.")
# @click.option(
#     "-f",
#     default=None,
#     help="",
# )
@click.argument("file", type=click.Path(exists=True))
def puppet(file):
    click.echo(f"Reading file: {file}")
