from click.testing import CliRunner
from exify.cli import cli


def test_help_flag():
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    expected_text = "Exify"
    assert result.exit_code == 0
    assert expected_text in result.output


def test_version_flag():
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    expected_text = "version"
    assert result.exit_code == 0
    assert expected_text in result.output
