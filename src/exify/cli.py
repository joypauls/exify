"""This is largely a dev utility for now, but it will be the primary entry point for the app."""

import click

HELP_TEXT = "Planetary Flow v0.1.0"


##########################
# Primary User Interface #
##########################


@click.group(help=HELP_TEXT)
def cli() -> None:
    """Container object for the app"""
    click.echo("<CLI Root> beep boop")


# @click.group(invoke_without_command=True)
# @click.option('--name', '-n', default='World', help="Name to greet if no subcommand is provided.")
# @click.pass_context
# def cli(ctx, name):
#     """A CLI tool for [Your Tool Description].

#     Usage:
#       mytool <argument>       Root level command.
#       mytool greet --name NAME  Greet someone with a custom message.
#     """
#     if ctx.invoked_subcommand is None:
#         # Root-level command behavior: Greet the user with the name provided.
#         click.echo(f"Hello, {name}!")
#     else:
#         # If a subcommand is called, this block is skipped.
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


@cli.command()
# @click.option(
#     "-f",
#     default=None,
#     help="",
# )
@click.argument("file", type=click.Path(exists=True))
def puppet(file):
    click.echo(f"Reading file: {file}")
